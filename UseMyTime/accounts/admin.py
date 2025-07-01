from django.contrib import admin
from .models import Profile

# Добавление профиля в админку
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']
    raw_id_fields = ['user']