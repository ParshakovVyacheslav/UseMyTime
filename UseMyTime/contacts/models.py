from django.db import models
from django.core.validators import RegexValidator

# Модель контактов (отображаются на главной странице контактов)
class Contact(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    surname = models.CharField(max_length=200, blank=True, null=True, verbose_name='Отчество')
    position = models.CharField(max_length=200, verbose_name='Должность')
    email = models.EmailField(verbose_name='Email', blank=True, null=True, unique=True)

    phone_validator = RegexValidator(
        regex=r'^(\+7|8)\d{10}$',
        message="Номер должен быть в формате: '+79998887766' или '89998887766'." 
    )
    phone = models.CharField(
        max_length=12,
        validators=[phone_validator],
        unique=True,
        verbose_name='Номер телефона',
        blank=True,
        null=True
    )

    def get_formatted_phone(self):
        phone = self.phone
        if not phone: return ''
        if phone.startswith('8'):
            phone = '+7' + phone[1:]
        return f'{phone[:2]} ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:]}'
    
    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.surname}'
    
    def __str__(self):
        return self.get_full_name()
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
    
# Модель для вопросов разработчикам
class Question(models.Model):
    name = models.CharField(max_length=600, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    body = models.TextField(verbose_name='Текст сообщения')
    is_closed = models.BooleanField(verbose_name='Закрыт', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'