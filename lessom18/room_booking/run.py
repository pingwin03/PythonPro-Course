from app import create_app
from app.models import db, User, Room, Equipment, Booking
from datetime import datetime, timedelta
import random

app = create_app()

def seed_database():
    with app.app_context():
        if User.query.first():
            print("Baza już zawiera dane. Pomijam seeding.")
            return
        
        print("Tworzenie przykładowych danych...")
        
        equipment_list = [
            Equipment(name="Projektor", icon="projector"),
            Equipment(name="Tablica", icon="chalkboard"),
            Equipment(name="Wideokonferencja", icon="video"),
            Equipment(name="Klimatyzacja", icon="snowflake"),
            Equipment(name="Nagłośnienie", icon="volume-up"),
        ]
        db.session.add_all(equipment_list)
        
        rooms = [
            Room(name="Sala A1", capacity=10, floor=1, description="Mała sala do spotkań", hourly_rate=50),
            Room(name="Sala B2", capacity=20, floor=2, description="Średnia sala z projektorem", hourly_rate=80),
            Room(name="Sala Konferencyjna", capacity=50, floor=3, description="Duża sala na prezentacje", hourly_rate=150),
            Room(name="Pokój Kreatywny", capacity=8, floor=1, description="Sala do burzy mózgów", hourly_rate=60),
        ]
        
        rooms[0].equipment = [equipment_list[1], equipment_list[3]]
        rooms[1].equipment = [equipment_list[0], equipment_list[2], equipment_list[3]]
        rooms[2].equipment = equipment_list
        rooms[3].equipment = [equipment_list[1]]
        
        db.session.add_all(rooms)
        
        users = [
            User(name="Jan Kowalski", email="jan@firma.pl", department="IT"),
            User(name="Anna Nowak", email="anna@firma.pl", department="HR"),
            User(name="Piotr Wiśniewski", email="piotr@firma.pl", department="Marketing"),
            User(name="Maria Dąbrowska", email="maria@firma.pl", department="IT", is_admin=True),
        ]
        db.session.add_all(users)
        db.session.commit()
        
        titles = ["Spotkanie zespołu", "Code review", "Planning sprint", "Retrospektywa", "Demo dla klienta"]
        now = datetime.now().replace(minute=0, second=0, microsecond=0)
        
        for i in range(20):
            room = random.choice(rooms)
            user = random.choice(users)
            days_offset = random.randint(0, 14)
            hour = random.randint(9, 16)
            duration = random.choice([1, 2, 3])
            
            start = now + timedelta(days=days_offset, hours=hour - now.hour)
            end = start + timedelta(hours=duration)
            
            if room.is_available(start, end):
                booking = Booking(
                    room=room,
                    user=user,
                    title=random.choice(titles),
                    start_time=start,
                    end_time=end,
                    attendees_count=random.randint(2, room.capacity)
                )
                db.session.add(booking)
        
        db.session.commit()
        print("✅ Baza danych wypełniona przykładowymi danymi!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_database()
    
    app.run(debug=True, port=5000)