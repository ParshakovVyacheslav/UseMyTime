from django.contrib import admin
from .models import WorkProgram

@admin.register(WorkProgram)
class WorkProgramAdmin(admin.ModelAdmin):
    exclude = ['users']