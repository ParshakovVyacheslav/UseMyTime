from django.contrib import admin
from .models import Task, Project

# Добавление задач и проектов в админку
admin.site.register(Task)
admin.site.register(Project)
