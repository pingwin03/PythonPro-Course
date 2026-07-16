import time
from sqlalchemy.engine import Engine
from flask import Blueprint, render_template, jsonify
from datetime import datetime, timedelta
from sqlalchemy import func, desc, event
from sqlalchemy.orm import joinedload
from app.models import db, Room, Booking, User, get_booking_statistics, Notification

dashboard_bp = Blueprint('dashboard', __name__)

# --- GLOBALNY LICZNIK ZAPYTAŃ DO DEBUGOWANIA N+1 ---
query_count = 0

@event.listens_for(Engine, "before_cursor_execute")  # <--- Zmiana z db.engine na Engine
def count_queries(conn, cursor, statement, parameters, context, executemany):
    global query_count
    query_count += 1


@dashboard_bp.route('/dashboard')
def dashboard():
    """Strona główna dashboardu ze statystykami i wykresami."""
    
    # Statystyki ogólne
    stats = {
        'total_rooms': Room.query.filter_by(is_active=True).count(),
        'total_users': User.query.count(),
        'total_bookings': Booking.query.filter_by(status='confirmed').count(),
        'bookings_today': Booking.query.filter(
            func.date(Booking.start_time) == datetime.today().date(),
            Booking.status == 'confirmed'
        ).count()
    }
    
    # Najbliższe rezerwacje (następne 24h)
    now = datetime.now()
    upcoming = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).filter(
        Booking.start_time >= now,
        Booking.start_time <= now + timedelta(hours=24),
        Booking.status == 'confirmed'
    ).order_by(Booking.start_time).limit(10).all()
    
    # Top użytkownicy (najwięcej rezerwacji)
    top_users = db.session.query(
        User.name,
        func.count(Booking.id).label('booking_count')
    ).join(Booking).filter(
        Booking.status != 'cancelled'
    ).group_by(User.id).order_by(desc('booking_count')).limit(5).all()
    
    # Wykorzystanie sal (% czasu zarezerwowanego w ostatnim miesiącu)
    month_ago = now - timedelta(days=30)
    room_utilization = []
    active_rooms = Room.query.filter_by(is_active=True).all()
    
    for room in active_rooms:
        total_hours = db.session.query(
            func.sum(
                func.extract('epoch', Booking.end_time - Booking.start_time) / 3600
            )
        ).filter(
            Booking.room_id == room.id,
            Booking.start_time >= month_ago,
            Booking.status != 'cancelled'
        ).scalar() or 0
        
        max_hours = 176
        utilization = (total_hours / max_hours) * 100
        
        room_utilization.append({
            'room': room.name,
            'hours': round(total_hours, 1),
            'utilization': round(utilization, 1)
        })
        
    room_utilization.sort(key=lambda x: x['utilization'], reverse=True)
    
    # --- ZADANIE 3: Statystyki departamentów dla wykresu ---
    dept_stats = db.session.query(
        User.department,
        func.count(Booking.id).label('booking_count')
    ).join(Booking).filter(
        Booking.status != 'cancelled'
    ).group_by(User.department).all()
    
    departments = [dept if dept else 'Nieokreślony' for dept, _ in dept_stats]
    dept_counts = [count for _, count in dept_stats]
    
    # --- ZADANIE 3: Statystyki godzinowe dla wykresu ---
    hour_stats = db.session.query(
        func.extract('hour', Booking.start_time).label('hour'),
        func.count(Booking.id).label('count')
    ).filter(
        Booking.status != 'cancelled'
    ).group_by('hour').order_by('hour').all()
    
    hours = [f"{int(hour)}:00" for hour, _ in hour_stats]
    hour_counts = [count for _, count in hour_stats]
    # --- ZADANIE 4: Pobranie nieprzeczytanych powiadomień dla zalogowanego admina (ID: 4) ---
    unread_notifications = Notification.query.filter_by(
        user_id=4, 
        is_read=False
    ).order_by(Notification.created_at.desc()).all()
    
    return render_template(
        'dashboard.html',
        stats=stats,
        upcoming=upcoming,
        top_users=top_users,
        room_utilization=room_utilization,
        departments=departments,
        dept_counts=dept_counts,
        hours=hours,
        hour_counts=hour_counts,
        # Przekazujemy powiadomienia do szablonu HTML
        notifications=unread_notifications
    )
        


@dashboard_bp.route('/api/dashboard/stats')
def api_stats():
    """API endpoint dla statystyk (do wykresów JS)."""
    # Pobieramy podstawowe statystyki z modelu
    stats = get_booking_statistics()
    
    # 1. Statystyki per departament (Zadanie 3)
    # Łączymy Booking z User, grupujemy po departamencie i liczymy wystąpienia
    dept_stats = db.session.query(
        User.department,
        func.count(Booking.id).label('booking_count')
    ).join(Booking).filter(
        Booking.status != 'cancelled'
    ).group_by(User.department).all()
    
    stats['department_stats'] = [
        {
            'department': dept if dept else 'Nieokreślony',
            'count': count
        }
        for dept, count in dept_stats
    ]
    
    # 2. Najpopularniejsze godziny rezerwacji (Zadanie 3)
    # Wyciągamy godzinę z start_time, grupujemy i liczymy
    hour_stats = db.session.query(
        func.extract('hour', Booking.start_time).label('hour'),
        func.count(Booking.id).label('count')
    ).filter(
        Booking.status != 'cancelled'
    ).group_by('hour').order_by('hour').all()
    
    stats['hourly_stats'] = [
        {
            'hour': f"{int(hour)}:00",
            'count': count
        }
        for hour, count in hour_stats
    ]
    
    return jsonify(stats)


@dashboard_bp.route('/test-db')
def test_db():
    """Testuje połączenie z bazą PostgreSQL."""
    try:
        db.session.execute(db.text('SELECT 1'))
        return "✅ Połączenie z PostgreSQL OK!"
    except Exception as e:
        return f"❌ Błąd połączenia: {str(e)}", 500


# ==========================================
#   ZADANIE 2: ENDPOINT DEBUGOWANIA N+1
# ==========================================
@dashboard_bp.route('/debug/n-plus-1')
def debug_n_plus_1():
    """Porównanie wydajności: Zapytanie N+1 vs Eager Loading."""
    global query_count
    
    # ----------------------------------------------------
    # ❌ TEST 1: Powolny sposób (Problem N+1)
    # ----------------------------------------------------
    query_count = 0  # Reset licznika
    start_time = time.time()
    
    # Pobieramy same rezerwacje (bez dołączania relacji pokoju i użytkownika)
    bookings_bad = Booking.query.all()
    
    bad_list = []
    for b in bookings_bad:
        # Każde odwołanie do b.room i b.user generuje NOWE ukryte zapytanie SQL!
        bad_list.append({
            'booking_title': b.title,
            'room_name': b.room.name,
            'user_name': b.user.name
        })
        
    bad_duration = time.time() - start_time
    bad_queries = query_count

    # ----------------------------------------------------
    # ✅ TEST 2: Szybki sposób (Eager Loading z joinedload)
    # ----------------------------------------------------
    query_count = 0  # Reset licznika
    start_time = time.time()
    
    # Dołączamy relacje od razu w jednym zapytaniu za pomocą joinedload
    bookings_good = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).all()
    
    good_list = []
    for b in bookings_good:
        # Dane są już załadowane w pamięci, brak dodatkowych zapytań SQL!
        good_list.append({
            'booking_title': b.title,
            'room_name': b.room.name,
            'user_name': b.user.name
        })
        
    good_duration = time.time() - start_time
    good_queries = query_count

    # Zwracamy porównanie wydajności w formacie JSON
    return jsonify({
        'status': 'success',
        'comparison': {
            'without_optimization_n_plus_1': {
                'queries_executed': bad_queries,
                'execution_time_ms': round(bad_duration * 1000, 2),
                'description': 'Pobrano rezerwacje, a następnie osobno dopytywano o salę i użytkownika dla każdego rekordu.'
            },
            'with_optimization_joinedload': {
                'queries_executed': good_queries,
                'execution_time_ms': round(good_duration * 1000, 2),
                'description': 'Pobrano rezerwacje razem z salą i użytkownikiem za pomocą jednego zapytania LEFT JOIN.'
            },
            'performance_gain': {
                'queries_saved': bad_queries - good_queries,
                'speedup_factor': round(bad_duration / good_duration, 2) if good_duration > 0 else 0
            }
        }
    })