from django.db import models
from django.conf import settings
from work_programs.models import WorkProgram
from datetime import timedelta

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='projects')
    title = models.CharField(max_length=200, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    total_time = models.DurationField(default=timedelta(0))
    programs = models.ManyToManyField(
        WorkProgram,
        through='ProjectProgram',
        through_fields=['project', 'program']
    )

    def get_hours_minutes(self):
        seconds = int(self.total_time.total_seconds())
        return [seconds // 3600, (seconds % 3600) // 60] # [hours, minutes]

class ProjectProgram(models.Model):
    program = models.ForeignKey(WorkProgram, 
                                on_delete=models.CASCADE,
                                related_name='project_programs')
    project = models.ForeignKey(Project, 
                                on_delete=models.CASCADE,
                                related_name='project_programs')
    total_time = models.DurationField(default=timedelta(0))

    def get_hours_minutes(self):
        seconds = int(self.total_time.total_seconds())
        return [seconds // 3600, (seconds % 3600) // 60] # [hours, minutes]

class ActiveProject(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='active_project')
    project = models.ForeignKey(Project, 
                                on_delete=models.CASCADE, 
                                null=True, blank=True)
    current_program = models.ForeignKey(WorkProgram,
                                        on_delete=models.SET_NULL,
                                        null=True, blank=True)
    in_work = models.BooleanField(default=False)
    last_started_at = models.DateTimeField(auto_now=True)
