from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    surname = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True,
                              verbose_name='Фото')
    
    def __str__(self):
        return f'Profile of {self.user.username}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'