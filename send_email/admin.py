from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class CantactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    
