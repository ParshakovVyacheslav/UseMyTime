from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Contact
from .forms import QuestionForm

# Главная страница контактов
def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {'contacts': contacts})

# Задание вопроса разработчикам (можно посмотреть в админке)
def ask(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contacts/ask_success.html', {'form': form})
        return HttpResponseRedirect(reverse_lazy('contacts'))
    else:
        return HttpResponseRedirect(reverse_lazy('contacts'))

