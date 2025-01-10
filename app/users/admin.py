from django.contrib import admin
from app.users.models import Role, User

class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "role", "manager")
    list_filter = ("role",)
    search_fields = ("email", "first_name", "last_name")
  
admin.site.register(User, UserAdmin)
admin.site.register(Role)