from django.db import models
from django.conf import settings

class WorkProgram(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                   related_name='work_programs')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'
    
