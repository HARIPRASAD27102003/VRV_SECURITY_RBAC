from django.contrib import admin
from .models import Permission , Role,User

# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
  list_display = ['pk', 'name']

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
  list_display = ['pk', 'name']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ['pk','username']
