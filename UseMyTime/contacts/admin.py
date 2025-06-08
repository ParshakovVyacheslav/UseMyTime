from django.contrib import admin
from .models import Question, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['get_full_name_coloumn', 'get_formatted_phone_coloumn', 'email', 'position']

    @admin.display(description='ФИО')
    def get_full_name_coloumn(self, obj):
        return obj.get_full_name()
    @admin.display(description='Номер телефона')
    def get_formatted_phone_coloumn(self, obj):
        return obj.get_formatted_phone()

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_closed', 'created_at']