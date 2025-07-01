from django.contrib import admin
from .models import Question, Contact

# Добавление контактов в админку
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['get_full_name_coloumn', 'get_formatted_phone_coloumn', 'email', 'position']

    # Отображение полного имени
    @admin.display(description='ФИО')
    def get_full_name_coloumn(self, obj):
        return obj.get_full_name()
    # Корректное отображение номера телефона
    @admin.display(description='Номер телефона')
    def get_formatted_phone_coloumn(self, obj):
        return obj.get_formatted_phone()

# Добавление вопросов в админку
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_closed', 'created_at']