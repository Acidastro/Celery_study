from Celery_study.celery import app
from .service import send


@app.task
def send_email(user_email):
    send(user_email)

# celery -A tasks worker --pool=solo --loglevel=info # запуск воркера
# data = background.delay(3)    # задача вызывается с помощью .delay
# data.status   # статус выполнения задачи
# data.id   # идентефикатор задачи
# data.get()    # результат задачи
# from celery.result import AsyncResult
# res = AsyncResult(data.id)    # async result
# res.status    # async status
