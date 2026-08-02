

# Importuję moją aplikację Celery, aby była dostępna przy starcie
from .celery import app as celery_app

__all__ = ('celery_app',)