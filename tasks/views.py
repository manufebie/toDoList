from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm

@login_required
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/task_list.html', context)

@login_required
def add_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
    return redirect('tasks:list')

@login_required
def task_completed(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.complete = True
    task.save()

    return redirect('tasks:list')

@login_required
def delete_completed_task(request):
    Task.objects.filter(complete__exact=True).delete()

    return redirect('tasks:list')


