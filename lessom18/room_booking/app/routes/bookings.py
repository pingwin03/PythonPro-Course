import uuid
from flask import Blueprint, jsonify, request, render_template
from datetime import datetime
from app.models import db, Booking, Room, User
from dateutil.rrule import rrule, DAILY, WEEKLY
from datetime import timedelta
from flask import send_file
from fpdf import FPDF
import io
import matplotlib
matplotlib.use('Agg')  # Wyłączenie GUI dla matplotlib (wymagane na serwerach)
import matplotlib.pyplot as plt
from sqlalchemy import func
from sqlalchemy.orm import joinedload

# Importy z biblioteki ReportLab
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

from app.models import Booking, Room, User

bookings_bp = Blueprint('bookings', __name__, url_prefix='/api/bookings')

@bookings_bp.route('/', methods=['GET'])
def get_bookings():
    from sqlalchemy.orm import joinedload
    query = Booking.query.options(joinedload(Booking.room), joinedload(Booking.user))
    
    if room_id := request.args.get('room_id'):
        query = query.filter(Booking.room_id == room_id)
    if user_id := request.args.get('user_id'):
        query = query.filter(Booking.user_id == user_id)
    if date_str := request.args.get('date'):
        date = datetime.strptime(date_str, '%Y-%m-%d')
        query = query.filter(db.func.date(Booking.start_time) == date.date())
    if status := request.args.get('status'):
        query = query.filter(Booking.status == status)
    
    query = query.order_by(Booking.start_time.desc())
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    pagination = query.paginate(page=page, per_page=per_page)
    
    return jsonify({
        'bookings': [b.to_dict(include_room=True, include_user=True) for b in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    })

@bookings_bp.route('/', methods=['POST'])
def create_booking():
    data = request.get_json()
    required = ['room_id', 'user_id', 'title', 'start_time', 'end_time']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Brak wymaganego pola: {field}'}), 400
    
    try:
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])
    except ValueError:
        return jsonify({'error': 'Niepoprawny format daty. Użyj ISO format.'}), 400
    
    if start_time >= end_time:
        return jsonify({'error': 'Czas rozpoczęcia musi być przed czasem zakończenia'}), 400
    if start_time < datetime.now():
        return jsonify({'error': 'Nie można rezerwować w przeszłości'}), 400
    
    room = Room.query.get(data['room_id'])
    if not room or not room.is_active:
        return jsonify({'error': 'Sala nie istnieje lub jest nieaktywna'}), 404
    
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({'error': 'Użytkownik nie istnieje'}), 404
    
    if not room.is_available(start_time, end_time):
        return jsonify({'error': 'Sala jest już zarezerwowana w tym czasie'}), 409
    
    attendees = data.get('attendees_count', 1)
    if attendees > room.capacity:
        return jsonify({'error': f'Zbyt wielu uczestników. Pojemność sali: {room.capacity}'}), 400
    
    try:
        booking = Booking(
            room_id=room.id,
            user_id=user.id,
            title=data['title'],
            description=data.get('description'),
            start_time=start_time,
            end_time=end_time,
            attendees_count=attendees
        )
        db.session.add(booking)
        db.session.commit()
        return jsonify({'message': 'Rezerwacja utworzona', 'booking': booking.to_dict(include_room=True)}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Błąd tworzenia rezerwacji: {str(e)}'}), 500


@bookings_bp.route('/recurring', methods=['POST'])
def create_recurring_booking():
    """
    Tworzy serię rezerwacji cyklicznych.
    
    Body JSON:
        room_id: int
        user_id: int
        title: str
        start_time: str (ISO format - pierwsze wystąpienie)
        end_time: str (ISO format - koniec pierwszego wystąpienia)
        recurrence_rule: str ("DAILY", "WEEKLY", "BIWEEKLY")
        recurrence_end: str (ISO format - data końcowa serii)
        description: str (optional)
        attendees_count: int (optional)
    """
    data = request.get_json()
    
    # Podstawowa walidacja pól cykliczności
    required = ['room_id', 'user_id', 'title', 'start_time', 'end_time', 'recurrence_rule', 'recurrence_end']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Brak wymaganego pola: {field}'}), 400
            
    try:
        first_start = datetime.fromisoformat(data['start_time'])
        first_end = datetime.fromisoformat(data['end_time'])
        recurrence_end = datetime.fromisoformat(data['recurrence_end'])
    except ValueError:
        return jsonify({'error': 'Niepoprawny format daty. Użyj ISO format.'}), 400
        
    rule_type = data['recurrence_rule'].upper()
    if rule_type not in ['DAILY', 'WEEKLY', 'BIWEEKLY']:
        return jsonify({'error': 'Niepoprawna reguła cyklu. Dozwolone: DAILY, WEEKLY, BIWEEKLY'}), 400
        
    if first_start >= first_end:
        return jsonify({'error': 'Czas rozpoczęcia musi być przed czasem zakończenia'}), 400
        
    if recurrence_end <= first_start:
        return jsonify({'error': 'Data zakończenia serii musi być po pierwszym wystąpieniu'}), 400

    # Mapowanie reguły na stałe biblioteki rrule
    freq_map = {
        'DAILY': DAILY,
        'WEEKLY': WEEKLY,
        'BIWEEKLY': WEEKLY  # Dla BIWEEKLY użyjemy WEEKLY z parametrem interval=2
    }
    
    interval = 2 if rule_type == 'BIWEEKLY' else 1
    
    # Generujemy listę dat rozpoczęcia serii przy użyciu rrule
    start_dates = list(rrule(
        freq=freq_map[rule_type],
        interval=interval,
        dtstart=first_start,
        until=recurrence_end
    ))
    
    # Wyliczamy czas trwania pojedynczego spotkania
    meeting_duration = first_end - first_start
    
    # Generujemy pary (start, end) dla każdego wystąpienia
    occurrences = [(start, start + meeting_duration) for start in start_dates]
    
    # Sprawdzamy czy sala i użytkownik istnieją
    room = Room.query.get(data['room_id'])
    if not room or not room.is_active:
        return jsonify({'error': 'Sala nie istnieje lub jest nieaktywna'}), 404
        
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({'error': 'Użytkownik nie istnieje'}), 404
        
    # Walidacja pojemności
    attendees = data.get('attendees_count', 1)
    if attendees > room.capacity:
        return jsonify({'error': f'Zbyt wielu uczestników. Pojemność: {room.capacity}'}), 400

    # Generujemy jeden wspólny identyfikator serii
    series_uuid = str(uuid.uuid4())
    created_bookings = []
    
    try:
        # Sprawdzamy konflikty i przygotowujemy obiekty
        for start, end in occurrences:
            if not room.is_available(start, end):
                # Jeśli choć jedno wystąpienie powoduje konflikt, zwracamy błąd
                return jsonify({
                    'error': f'Konflikt rezerwacji! Sala jest już zajęta w terminie {start.strftime("%Y-%m-%d %H:%M")} - {end.strftime("%H:%M")}.',
                    'conflict_date': start.isoformat()
                }), 409
                
            booking = Booking(
                room_id=room.id,
                user_id=user.id,
                title=data['title'],
                description=data.get('description'),
                start_time=start,
                end_time=end,
                attendees_count=attendees,
                recurrence_rule=rule_type,
                series_id=series_uuid
            )
            db.session.add(booking)
            created_bookings.append(booking)
            
        # Zapisujemy całą serię w bazie (transakcja: wszystko albo nic!)
        db.session.commit()
        
        return jsonify({
            'message': f'Pomyślnie utworzono serię {len(created_bookings)} rezerwacji.',
            'series_id': series_uuid,
            'bookings': [b.to_dict() for b in created_bookings]
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Błąd podczas zapisu serii: {str(e)}'}), 500


# ===================================================
#   ZMODYFIKOWANY ENDPOINT USUWANIA (POJEDYNCZO LUB CAŁEJ SERII)
# ===================================================
# Podmieniamy lub rozbudowujemy istniejący endpoint DELETE:
@bookings_bp.route('/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    """
    Anuluje rezerwację.
    
    Query params:
        all_series: bool (optional, domyślnie false. Jeśli true, anuluje całą serię rezerwacji)
    """
    booking = Booking.query.get_or_404(booking_id)
    cancel_all_series = request.args.get('all_series', 'false').lower() in ['true', '1', 'yes']
    
    if booking.status == 'cancelled':
        return jsonify({'error': 'Rezerwacja już wcześniej została anulowana'}), 400
        
    try:
        if cancel_all_series and booking.series_id:
            # Anulujemy wszystkie nadchodzące rezerwacje z tej serii
            future_series_bookings = Booking.query.filter(
                Booking.series_id == booking.series_id,
                Booking.start_time >= datetime.now(),
                Booking.status != 'cancelled'
            ).all()
            
            for b in future_series_bookings:
                b.status = 'cancelled'
                
            db.session.commit()
            return jsonify({
                'message': f'Anulowano całą serię rezerwacji. Liczba anulowanych spotkań: {len(future_series_bookings)}.'
            })
        else:
            # Anulujemy tylko to jedno pojedyncze wystąpienie
            if booking.start_time < datetime.now():
                return jsonify({'error': 'Nie można anulować rezerwacji z przeszłości'}), 400
                
            booking.status = 'cancelled'
            db.session.commit()
            return jsonify({'message': 'Pomyślnie anulowano pojedynczą rezerwację.'})
            
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Błąd anulowania: {str(e)}'}), 500
    
    
# ===================================================
#   ZADANIE 6: OFICJALNY MIESIĘCZNY RAPORT PDF (ReportLab)
# ===================================================

@bookings_bp.route('/reports/monthly', methods=['GET'])
def generate_monthly_report_pdf():
    """
    Generuje miesięczny raport PDF.
    Endpoint: /api/bookings/reports/monthly?month=YYYY-MM
    """
    # 1. Pobranie i walidacja parametru 'month' (np. "2026-08")
    month_param = request.args.get('month')
    if not month_param:
        return jsonify({'error': 'Brak wymaganego parametru query: month (format YYYY-MM)'}), 400
        
    try:
        year, month = map(int, month_param.split('-'))
    except ValueError:
        return jsonify({'error': 'Niepoprawny format parametru month. Użyj formatu YYYY-MM'}), 400

    # Obliczamy zakres dat dla wybranego miesiąca
    from datetime import datetime
    import calendar
    
    start_date = datetime(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    end_date = datetime(year, month, last_day, 23, 59, 59)

    # --- POBIERANIE DANYCH Z BAZY ---
    # Wszystkie potwierdzone rezerwacje w danym miesiącu
    monthly_bookings = Booking.query.options(joinedload(Booking.room)).filter(
        Booking.start_time >= start_date,
        Booking.start_time <= end_date,
        Booking.status == 'confirmed'
    ).all()

    # Statystyki ogólne
    total_bookings = len(monthly_bookings)
    total_hours = sum(b.duration_hours for b in monthly_bookings)
    total_revenue = sum(b.total_cost for b in monthly_bookings)

    # Top 10 sal (wg liczby rezerwacji)
    top_rooms_query = db.session.query(
        Room.name,
        func.count(Booking.id).label('booking_count'),
        func.sum(func.extract('epoch', Booking.end_time - Booking.start_time) / 3600).label('total_hours')
    ).join(Booking).filter(
        Booking.start_time >= start_date,
        Booking.start_time <= end_date,
        Booking.status == 'confirmed'
    ).group_by(Room.id).order_by(func.count(Booking.id).desc()).limit(10).all()

    # Top 10 użytkowników (wg liczby rezerwacji i wydatków)
    top_users_query = db.session.query(
        User.name,
        func.count(Booking.id).label('booking_count'),
        func.sum(func.extract('epoch', Booking.end_time - Booking.start_time) / 3600).label('total_hours')
    ).join(Booking).filter(
        Booking.start_time >= start_date,
        Booking.start_time <= end_date,
        Booking.status == 'confirmed'
    ).group_by(User.id).order_by(func.count(Booking.id).desc()).limit(10).all()

    # --- GENEROWANIE WYKRESU (MATPLOTLIB) ---
    # Wykres słupkowy: Wykorzystanie sal (godziny)
    room_names_chart = [r[0] for r in top_rooms_query[:5]]  # Bierzemy top 5 do wykresu
    room_hours_chart = [float(r[2]) if r[2] else 0.0 for r in top_rooms_query[:5]]

    chart_img_io = io.BytesIO()
    
    if room_names_chart:
        plt.figure(figsize=(6, 3))
        plt.bar(room_names_chart, room_hours_chart, color='#646ee6')
        plt.title('Wykorzystanie sal w godzinach (Top 5)', fontsize=10, fontweight='bold')
        plt.ylabel('Godziny', fontsize=8)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.tight_layout()
        plt.savefig(chart_img_io, format='png', dpi=150)
        plt.close()
        chart_img_io.seek(0)

    # Rejestracja systemowej czcionki Arial (z pełnym wsparciem UTF-8 / PL znaków)
    font_dir = "C:\\Windows\\Fonts"
    arial_path = os.path.join(font_dir, "arial.ttf")
    arial_bold_path = os.path.join(font_dir, "arialbd.ttf")

    if os.path.exists(arial_path) and os.path.exists(arial_bold_path):
        pdfmetrics.registerFont(TTFont('ArialCustom', arial_path))
        pdfmetrics.registerFont(TTFont('ArialCustom-Bold', arial_bold_path))
        font_regular = 'ArialCustom'
        font_bold = 'ArialCustom-Bold'
    else:
        # Fallback na standardową Helvetice (jeśli fonty Windows nie są dostępne)
        font_regular = 'Helvetica'
        font_bold = 'Helvetica-Bold'

    # --- GENEROWANIE RAPORTU PDF (REPORTLAB) ---
    pdf_buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'ReportTitle',
        parent=styles['Heading1'],
        fontName=font_bold,
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=15
    )
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontName=font_bold,
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#2980B9'),
        spaceBefore=12,
        spaceAfter=6
    )
    normal_style = ParagraphStyle(
        'ReportNormal',
        parent=styles['Normal'],
        fontName=font_regular,
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#2C3E50')
    )

    story = []

    # 1. Tytuł i nagłówek
    story.append(Paragraph(f"Miesięczny Raport Rozliczeniowy: {month_param}", title_style))
    story.append(Paragraph(f"Wygenerowano automatycznie dnia: {datetime.now().strftime('%Y-%m-%d %H:%M')}", normal_style))
    story.append(Spacer(1, 15))

    # 2. Podsumowanie (Kluczowe wskaźniki)
    story.append(Paragraph("1. Podsumowanie aktywności", section_style))
    summary_data = [
        [Paragraph("<b>Wskaźnik</b>", normal_style), Paragraph("<b>Wartość</b>", normal_style)],
        [Paragraph("Liczba wszystkich rezerwacji", normal_style), Paragraph(f"{total_bookings} spotkań", normal_style)],
        [Paragraph("Łączny czas trwania", normal_style), Paragraph(f"{round(total_hours, 1)} godzin", normal_style)],
        [Paragraph("Całkowity wygenerowany przychód", normal_style), Paragraph(f"{round(total_revenue, 2)} PLN", normal_style)]
    ]
    summary_table = Table(summary_data, colWidths=[250, 250])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#ECF0F1')),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#BDC3C7')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 15))

    # 3. Wykres (jako obraz)
    if room_names_chart:
        story.append(Paragraph("2. Wykres wykorzystania sal", section_style))
        story.append(Image(chart_img_io, width=350, height=175))
        story.append(Spacer(1, 15))

    # 4. Tabela: Top 10 sal
    story.append(Paragraph("3. Top 10 najczęściej rezerwowanych sal", section_style))
    rooms_table_data = [[
        Paragraph("<b>Nazwa sali</b>", normal_style), 
        Paragraph("<b>Liczba rezerwacji</b>", normal_style), 
        Paragraph("<b>Suma godzin</b>", normal_style)
    ]]
    
    for room_name, count, hours in top_rooms_query:
        rooms_table_data.append([
            Paragraph(room_name, normal_style),  # <--- OWINIĘTE W PARAGRAPH
            Paragraph(str(count), normal_style),
            Paragraph(str(round(hours, 1)) if hours else "0", normal_style)
        ])
        
    if len(rooms_table_data) == 1:
        rooms_table_data.append([Paragraph("Brak danych", normal_style), Paragraph("-", normal_style), Paragraph("-", normal_style)])
        
    rooms_table = Table(rooms_table_data, colWidths=[250, 125, 125])
    rooms_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EBF5FB')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#BDC3C7')),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(rooms_table)
    story.append(Spacer(1, 15))

    # 5. Tabela: Top 10 użytkowników
    story.append(Paragraph("4. Top 10 najbardziej aktywnych użytkowników", section_style))
    users_table_data = [[
        Paragraph("<b>Użytkownik</b>", normal_style), 
        Paragraph("<b>Liczba rezerwacji</b>", normal_style), 
        Paragraph("<b>Suma godzin</b>", normal_style)
    ]]
    
    for user_name, count, hours in top_users_query:
        users_table_data.append([
            Paragraph(user_name, normal_style),  # <--- OWINIĘTE W PARAGRAPH
            Paragraph(str(count), normal_style),
            Paragraph(str(round(hours, 1)) if hours else "0", normal_style)
        ])
        
    if len(users_table_data) == 1:
        users_table_data.append([Paragraph("Brak danych", normal_style), Paragraph("-", normal_style), Paragraph("-", normal_style)])
        
    users_table = Table(users_table_data, colWidths=[250, 125, 125])
    users_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EBF5FB')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#BDC3C7')),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(users_table)

    # Budujemy PDF
    doc.build(story)
    
    pdf_buffer.seek(0)
    return send_file(
        pdf_buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f"raport_miesieczny_{month_param}.pdf"
    )