# Celery_study

Шаблон использования
Celery+Redis+Django+Docker+

# Как начать:

`pip install celery redis`

1. Создать файл `celery.py` в каталоге рядом с `settings.py`
2. Внутри `celery.py` файла прописать:

    ```angular2html
    import os
    
    from celery import Celery
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
    app = Celery('proj')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks()
    
    @app.task(bind=True)
    def debug_task(self):
        print(f'Request: {self.request!r}')
    ```

3. Внутри `__init__.py` в каталоге рядом с `settings.py` прописать:

    ```angular2html
    from .celery import app as celery_app
    
    __all__ = ('celery_app',)
    ```
4. Внутри settings.py прописать:
    ```angular2html
    REDIS_HOST = 'localhost'
    REDIS_PORT = '6379'
    CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
    CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
    CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
   ```

5. Запуск redis в docker:
    ```
    docker run -p 6379:6379 --name redis-celery -d redis
    docker ps
    ```
6. Запуск celery:
    ```
   celery -A Celery_study worker -l info --pool=solo
   ```
7. Прверка тасков:
   ```angular2html
   from Celery_study.celery import debug_task
   debug_task.delay()
   # должно успешно выполниться
   ```

## Celery_result:

`pip install django-celery-results django-redis`

1. В `settings.py`:
   ```angular2html
   INSTALLED_APPS = (
    ...,
    'django_celery_results',
   )
   ```
2. Выполнить миграции:
   `python manage.py migrate django_celery_results`

3. Добавить настройки кеша в `settings.py`:
   ```angular2html
   CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
   }
   # взято из документации джанго
   
   CELERY_CACHE_BACKEND = 'default'
   ```

## Celery_beat

`pip install django-celery-beat`

1. `settings.py`:
   ```angular2html
   INSTALLED_APPS = (
       ...,
       'django_celery_beat',
   )
   
   CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
   ```
2. `python manage.py migrate`
3. Запуск:
   ```angular2html
   celery -A Celery_study beat -l info
   ```
