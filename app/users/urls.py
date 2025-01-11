from django.urls import path
from django.conf.urls.static import static
from app.users import views
from config import settings

app_name = 'users'

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("interns/", views.interns_list, name='interns_list'),
    path('interns/search/', views.search_interns, name='search_interns'),
    path('interns/add/<int:id>/', views.add_intern, name='add_intern'),
    path("<str:slug>/", views.view_profile, name="profile"),
    path("<str:slug>/edit-profile/", views.edit_profile, name="edit_profile"),
    path("<str:slug>/tasks_for_me/", views.tasks_for_me, name="tasks_for_me"),
    path("<str:slug>/author_tasks/", views.author_tasks, name="author_tasks"),
]