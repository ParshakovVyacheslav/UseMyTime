from django import forms
from .models import Question

# Форма вопроса разработчикам
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'email', 'body'] 