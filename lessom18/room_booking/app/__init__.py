from flask import Flask
from app.models import db
from config import config

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inicjalizacja bazy danych
    db.init_app(app)
    
    # --- TUTAJ IMPORTUJEMY BLUEPRINTY ---
    from app.routes.bookings import bookings_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.notifications import notifications_bp
    
    # --- TUTAJ REJESTRUJEMY BLUEPRINTY W APLIKACJI ---
    app.register_blueprint(bookings_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(notifications_bp)
    
    return app