from django.shortcuts import redirect, render
from django.urls import reverse
from django.core import serializers

from app.tasks.models import Task


def index(request):
    if not(request.user.is_authenticated):
        return redirect(reverse('users:login'))
    
    task = Task.objects.filter(worker=request.user)

    context = {
        'tasks': serializers.serialize('json', task)
    }

    return render(request, 'main/index.html', context)
