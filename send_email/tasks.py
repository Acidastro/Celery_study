from Celery_study.celery import app
from .models import Contact
from .service import send


@app.task
def send_email(user_email):
    send(user_email)


@app.task
def task_two():
    for contact in Contact.objects.all():
        send(contact.email)


@app.task
def task_three(a, b):
    return a * b


@app.task(
    bind=True,
    default_retry_delay=5 * 60,  # время через которое нужно запускать (в секундах)
)
def my_task_retry(self, x, y):
    try:
        return x + y
    except Exception as exc:  # если исключение, то перезапуск
        raise self.retry(
            exc=exc,
            countdown=60  # время через которое перезапустится
        )

# отложенный запуск настраивается через аргумент my_task.apply_async((args),countdown=60)

# my_task.apply_async((args), link=my_task.s(20)) # таска отработает и вызовет еще раз сама себя с помощью аргумента \
# link, далее результат первого выполнения передастся в первый аргумент.
#
# data = my_task.delay(3)    # задача вызывается с помощью .delay
# data.status   # статус выполнения задачи
# data.id   # идентефикатор задачи
# data.get()    # результат задачи
# from celery.result import AsyncResult
# res = AsyncResult(data.id)    # async result
# res.status    # async status
