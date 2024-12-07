"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views , viewApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sign_page,name="sign_page"),
    path('login/',views.login,name="login"),
    path('create_user/',views.create_user_page ,name="create_user_page"),
    path('logout/',views.logout ,name="logout"),
    path('home/',views.home ,name="home"),
    path('roles/',views.role_management ,name="role_management"),
    path('home/users/',views.user_management ,name="user_management"),
    path('roles/<int:pk>',views.detail_role ,name="detail_role"),
    path('roles/add_role',views.add_role ,name="add_role"),
    path('roles/remove_role',views.remove_role ,name="remove_role"),
    path('roles/edit_role',views.edit_role ,name="edit_role"),
    path('roles/edit_role/<int:pk>/',views.edit_role_id ,name="edit_role_id"),

    # Permissions
    path('permissions/',views.permission_management ,name="permission_management"),
    path('permissions/<int:pk>',views.detail_role ,name="detail_permission"),
    path('permissions/add_permission',views.add_permission ,name="add_permission"),
    path('permissions/edit_permission',views.edit_permission ,name="edit_permission"),
    path('permissions/remove_permission',views.remove_permission ,name="remove_permission"),

    # APIs
    path('api/roles/remove/<int:role_id>/',viewApi.api_remove_role ,name="api_remove_role"),
    path('api/roles/remove/<int:role_id>/<int:permission_id>/',viewApi.api_remove_role_permission ,name="api_remove_role_permission"),
]
