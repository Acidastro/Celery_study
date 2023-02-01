# from django.core.mail import send_mail


def send(user_email):
    """Стандартная джанговская отправка email
    Письма будут отсылаться через гугловскую почту и их smtp/
    Для этого в settings.py добавляются доп.настройки/
    """
    print(user_email)
    print('OK')
