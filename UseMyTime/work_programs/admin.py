from django.contrib import admin
from .models import WorkProgram

# Добавление программ в админку
@admin.register(WorkProgram)
class WorkProgramAdmin(admin.ModelAdmin):
    exclude = ['users']