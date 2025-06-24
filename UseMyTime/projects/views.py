from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Project, ProjectProgram, ActiveProject
from work_programs.models import WorkProgram

class ProjectCreateView(CreateView, LoginRequiredMixin):
    template_name = 'projects/create_update.html'
    model = Project
    fields = ['title', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})

class ProjectUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'projects/create_update.html'
    model = Project
    fields = ['title', 'description']
    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class ProjectDeleteView(DeleteView, LoginRequiredMixin):
    model = Project
    success_url = reverse_lazy('project_create')
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class ArchiveProjectListView(ListView, LoginRequiredMixin):
    template_name = 'projects/archive.html'
    model = Project
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).filter(is_archived=True)

class ProjectDetailView(DetailView, LoginRequiredMixin):
    template_name = 'projects/detail.html'
    model = Project
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

@require_POST
@login_required
def project_activate(request):
    active_project, _ = ActiveProject.objects.get_or_create(user=request.user)
    project_id = request.POST.get('project_id')
    try:
        project = Project.objects.get(id=project_id, user=request.user)
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'})
    active_project.project = project
    active_project.save()
    return HttpResponseRedirect(reverse_lazy('project_detail', kwargs={'pk': project_id}))

@require_POST
@login_required
def project_start(request):
    active_project = ActiveProject.objects.filter(user=request.user).first()
    if not active_project:
        return JsonResponse({'is_success': False, 
                             'error': 'Where is not active project'})
    if active_project.in_work:
        return JsonResponse({'is_success': False, 
                             'error': 'Project is already started'})
    current_program_id = request.POST.get('current_program_id', '')
    current_program = WorkProgram.objects.get(id=current_program_id) if current_program_id else None
    active_project.current_program = current_program
    active_project.in_work = True
    active_project.save()
    return JsonResponse({'is_success': True})

@require_POST
@login_required
def project_stop(request):
    active_project = ActiveProject.objects.filter(user=request.user).first()
    if not active_project or not active_project.project:
        return JsonResponse({'is_success': False, 
                             'error': 'Where is not active project'})
    if not active_project.in_work:
        return JsonResponse({'is_success': False, 
                             'error': 'Project is already stopped'})
    duration = timezone.now() - active_project.last_started_at
    active_project.in_work = False
    active_project.project.total_time += duration
    active_project.save()
    active_project.project.save()
    print(active_project.in_work)
    if active_project.current_program:
        project_program, _ = ProjectProgram.objects.get_or_create(program=active_project.current_program,
                                                                  project=active_project.project)
        project_program.total_time += duration
        project_program.save()
    return JsonResponse({'is_success': True})

@require_POST
@login_required
def project_archive(request, id):
    try:
        project = Project.objects.get(id=id, user=request.user)
        project.is_archived = True
        project.save()
        return HttpResponseRedirect(reverse_lazy('project_detail', kwargs={'pk': id}))
    except Project.DoesNotExist:
        return HttpResponseRedirect(reverse_lazy('project_detail', kwargs={'pk': id}))
