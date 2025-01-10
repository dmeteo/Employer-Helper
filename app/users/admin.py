from django.contrib import admin
from app.users.models import Role, User

class UserAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "surname")
  
admin.site.register(User, UserAdmin)
admin.site.register(Role)