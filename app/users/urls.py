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
    path('interns/search/', views.search_all_interns, name='search_all_interns'),
    path('interns/add/<int:id>/', views.add_intern, name='add_intern'),
    path('my-interns/', views.my_interns_list, name='my_interns'),
    path('my-interns/search/', views.search_my_interns, name='search_my_interns'),
    path("<str:slug>/", views.view_profile, name="profile"),
    path("<str:slug>/edit-profile/", views.edit_profile, name="edit_profile"),
    path("<str:slug>/tasks_for_me/", views.tasks_for_me, name="tasks_for_me"),
    path("<str:slug>/author_tasks/", views.author_tasks, name="author_tasks"),
]