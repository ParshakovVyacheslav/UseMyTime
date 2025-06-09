from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.programs, name='programs'),
    path('delete/<int:id>', views.program_delete, name='program_delete')
]