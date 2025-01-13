from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('notifications/', views.get_notifications, name='get_notifications'),
    path('read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
]