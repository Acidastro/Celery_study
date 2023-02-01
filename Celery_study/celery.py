from celery import Celery
import os
from celery.schedules import crontab

# запуск celery
# celery -A Celery_study worker -l info --pool=solo
# запуск flower через docker
# docker run -p 5555:5555 mher/flower
# запуск flower из терминала
# celery -A Celery_study flower --port=5555

#  где искать настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery_study.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

# create app
app = Celery('Celery_study', )

# настройка работы с джанго
app.config_from_object('django.conf:settings', namespace='CELERY', )

# автоматичкски подцепляет таски
app.autodiscover_tasks()

# настройка переодических тасков

# celery -A Celery_study beat -l info --pool=solo
app.conf.beat_schedule = {
    'send-spam-every-1-min': {
        'task': 'send_email.tasks.task_two',  # регистрируем таску
        'schedule': crontab(minute='*/1'),  # периодичность выполнения
    },
}
