from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import WorkProgram

@login_required
def programs(request):
    programs = WorkProgram.objects.all()
    search = request.GET.get('search', '')
    if search:
        programs = programs.filter(name__icontains=search)
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_programs')
        selected_programs = WorkProgram.objects.filter(id__in=selected_ids)
        for program in selected_programs:
            request.user.work_programs.add(program)
    selected_programs = request.user.work_programs.all()
    return render(request, 'work_programs/index.html', {'programs': programs,
                                                        'selected_programs': selected_programs,
                                                        'search': search}) 

@require_POST
@login_required
def program_delete(request, id):
    program = get_object_or_404(WorkProgram, id=id)
    request.user.work_programs.remove(program)
    return redirect(reverse_lazy('programs'))
