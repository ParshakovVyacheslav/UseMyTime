from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('update/<int:pk>', views.ProjectUpdateView.as_view(), name='project_update'),
    path('delete/<int:pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('detail/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('archive/', views.ArchiveProjectListView.as_view(), name='projects_archive'),
    path('archivate/<int:id>', views.project_archive, name='projects_archivate'),
    path('activate/', views.project_activate, name='projects_activate'),
    path('start/', views.project_start, name='projects_start'),
    path('stop/', views.project_stop, name='projects_stop'),
    path('task/<int:id>', views.change_task_status, name='change_task_status')
]
