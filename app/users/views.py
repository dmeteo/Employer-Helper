from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core import serializers

from app.tasks.models import Task
from app.users.models import Role, User
from app.users.forms import UserLoginForm, UserSignUpForm, UserForm

def login(request):
    if request.user.is_authenticated: 
        redirect(reverse('main:index'))
    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{email}, Вы вошли в аккаунт")
                return redirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/authorization.html', context)

def signup(request):
    if request.user.is_authenticated: 
        redirect(reverse('main:index'))
    elif request.method == 'POST':
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = Role.objects.get(id=1)
            user.save()

            user = form.instance

            messages.success(request, f"{user.email}, Вы успешно зарегистрированы и вошли в аккаунт")
            return redirect(reverse('users:login'))
    else:
        form = UserSignUpForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)
    

@login_required
def edit_profile(request, slug):
    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return redirect(reverse('users:profile'))
    else:
        form = UserForm(instance=request.user)  

    context = {
        'title': 'Редактирование профиля',
        'form': form,
        'slug': slug
    }
    return render(request, 'users/edit-profile.html', context)   


def view_profile(request, slug):
    user = get_object_or_404(User, slug=slug)

    context = {
        'title': 'Профиль',
        'email': user.email,
        'image': user.image,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'surname': user.surname,
        'phone_number': user.phone_number,
        'slug': slug
    }
    
    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.email}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))


@login_required
def author_tasks(request, slug):

    user = User.objects.get(slug=slug)
    
    context = {
        'title': 'Задачи которые вы поставили',
        'author_tasks': Task.objects.filter(author=user),
        'slug': slug
    }

    return render(request, 'tasks/author_tasks.html', context)


@login_required
def tasks_for_me(request, slug):

    user = User.objects.get(slug=slug)
    
    context = {
        'tasks': serializers.serialize('json', list(Task.objects.filter(worker=user))),
        'slug': slug
    }

    return render(request, 'tasks/tasks_for_me.html', context)


def add_intern(request, id):
    intern = User.objects.filter(id=id)
    intern.manager = request.user
    intern.save()


# def interns_list(request):
#     interns = User.objects.filter(level=1)
    
#     context = {
#         "interns": interns
#     }

#     return render(request, 'users/interns_list', context)


# def my_interns_list(request):
#     manager = User.objects.get(id=request.id)
#     interns = manager.subordinates.all()
    
#     context = {
#         "interns": interns
#     }

#     return render(request, 'users/interns_list', context)