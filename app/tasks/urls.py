from django.urls import path

from app.tasks import views

app_name = 'tasks'

urlpatterns = [
    path("create-task/", views.create_task, name="create-task"),
    path("edit-task/", views.edit_task, name="edit-task"),
    path("<int:pk>/", views.task_detail, name="task-detail"),
    path("delete-task/<int:id>/", views.delete_task, name="delete-task")
]