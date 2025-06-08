from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='profile_edit'),
]