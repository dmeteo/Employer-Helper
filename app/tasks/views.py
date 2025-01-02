from datetime import timezone
from pyexpat.errors import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from app.tasks.forms import TaskForm
from app.tasks.models import Task
from app.users.models import User


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
        users = User.objects.values('id', 'first_name')
        return JsonResponse(list(users), safe=False)
    if request.method == 'POST':
        selected_user_id = request.POST.get('user')
        if selected_user_id:
            try:
                selected_user = User.objects.get(id=selected_user_id)
                return render(request, 'users/profile.html', {'user': selected_user, 'slug': selected_user.slug})
            except User.DoesNotExist:
                return render(request, 'tasks/user_dropdown.html', {'error': 'Пользователь не найден'})
    return render(request, 'tasks/user_dropdown.html')
