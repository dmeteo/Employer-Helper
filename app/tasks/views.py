from datetime import timezone
from pyexpat.errors import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q

from app.tasks.forms import TaskForm
from app.tasks.models import Task
from app.users.models import User


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            worker_id = request.POST.get('worker')
            task.worker = User.objects.get(id=worker_id)
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


def complete_task(request, id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=id)
        task.status = True
        task.save()
        return redirect(reverse('main:index'))
    return redirect(reverse('main:index'))


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def user_list(request):
    if is_ajax(request=request):
        query = request.GET.get('q', '').strip()
        users = User.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(surname__icontains=query)
        ).values('id', 'first_name', 'last_name', 'surname')[:10]

        results = [
            {
                'id': user['id'],
                'text': f"{user['surname']} {user['first_name']} {user['last_name']}"
            } for user in users
        ]
        return JsonResponse({'results': results}, safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)
