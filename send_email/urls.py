from django.contrib import admin
from django.urls import path

from send_email.views import ContactView

urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
]
