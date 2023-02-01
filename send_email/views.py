from django.shortcuts import render
from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
# from .service import send_mail
from .tasks import send_email


class ContactView(CreateView):
    """Отображение формы подписки по email"""
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'mail/contact.html'

    def form_valid(self, form):
        form.save()
        send_email.delay(form.instance.email)
        # send_mail(form.instance.email)   # отправляет письмо
        return super().form_valid(form)
