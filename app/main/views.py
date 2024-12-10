from django.shortcuts import redirect, render
from django.urls import reverse

from app.tasks.models import Task




def index(request):
    if not(request.user.is_authenticated):
        return redirect(reverse('users:login'))
    
    task = Task.objects.filter(worker=request.user)

    context = {
        'title': 'Главная',
        'task': task
    }

    return render(request, 'main/index.html', context)
