from datetime import timezone
from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from app.tasks.forms import TaskForm
from app.tasks.models import Task


def create_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.worker = request.user
            task.status = False
            task.save()
            return redirect(reverse('main:index'))
    else:
        form = TaskForm()
    
    context = {
        'title': "Создание задачи",
        'form': form,
    }
    return render(request, 'tasks/create-task.html', context) 


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    context = {
        'title': "Подробности",
        'task': task
    }
    return render(request, "tasks/task_detail.html", context)


def edit_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task_form = TaskForm(data=request.POST, instance=task)
        if task_form.is_valid():
            task.save()
            messages.success(request, "Карточка проекта успешно обновлена")
            return HttpResponseRedirect(reverse(f'{request.task.id}'))
    else:
        task = task_form(instance=task)  

    context = {
        'title': 'Редактирование задачи',
        'task': task,
    }
    return render(request, 'tasks/edit-task.html', context)


def delete_task(request, id):
    task = Task.objects.filter(id=id)
    task.delete()
    return redirect(reverse('main:index'))