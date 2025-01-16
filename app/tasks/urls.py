from django.urls import path

from app.tasks import views

app_name = 'tasks'

urlpatterns = [
    path("create_task/for/me", views.create_task_for_me, name="create_task_for_me"),
    path("create_task/for/<str:slug>", views.create_task_for_other, name="create_task_for_other"),
    path("edit_task/", views.edit_task, name="edit_task"),
    path("<int:pk>/", views.task_detail, name="task_detail"),
    path("delete_task/<int:id>/", views.delete_task, name="delete_task"),
    path("complete_task/<int:id>/", views.complete_task, name="complete_task"),
    path('user_list/', views.user_list, name='user_list'),
]