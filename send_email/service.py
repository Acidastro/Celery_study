from django.core.mail import send_mail


def send(user_email):
    """Стандартная джанговская отправка email
    Письма будут отсылаться через гугловскую почту и их smtp/
    Для этого в settings.py добавляются доп.настройки/
    """
    send_mail(
        'Вы подписались на рассылку',
        'Вы подписались на рассылку',
        'mymail@gmail.com',
        [user_email],
        fail_silently=False
    )
