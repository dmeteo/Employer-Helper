from django.shortcuts import redirect, render
from django.urls import reverse
from django.core import serializers

from app.tasks.models import Task


def index(request):
    if not(request.user.is_authenticated):
        return redirect(reverse('users:login'))
    
    if (request.user.role.level > 1):
        return redirect(reverse('users:my_interns'))
    
    task = Task.objects.filter(worker=request.user)

    context = {
        'header': "Добро пожаловать, " + request.user.first_name,
        'tasks': serializers.serialize('json', task)
    }

    return render(request, 'main/index.html', context)
