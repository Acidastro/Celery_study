from celery import Celery
import os

# celery -A Celery_study worker -l info

#  где искать настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery_study.settings')

app = Celery(
    'Celery_study',
)

# настройка работы с джанго
app.config_from_object(
    'django.conf:settings',
    namespace='CELERY',
)

# автоматичкски подцепляет таски
app.autodiscover_tasks()
