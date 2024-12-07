from django.shortcuts import redirect
from django.http import HttpResponse
from core.models import User

def admin_only(view_func):
  def wrapper(request, *args, **kwargs):
    user_role = request.session.get('role')

    print(user_role)

    if user_role.lower().split() == 'admin':
      return view_func(request, *args, **kwargs)
    else:
      return HttpResponse('unauthorized')
    
  return wrapper

def check_logged_user(view_func):
  def wrapper(request, *args, **kwargs):
    username = request.session.get('username')
    if username is not None:
      user = User.objects.get(username=username)
      role = user.roles.name if user.roles else 'no_role'

      if role == 'admin':
        return redirect('home')
      elif role == 'role_manager':
        return redirect('role_management')
      elif role == 'customer':
        return HttpResponse('This is decorator customer')

    return view_func(request, *args, **kwargs)
  return wrapper

def admin_and_role_only(view_func):
  def wrapper(request, *args, **kwargs):
    user_role = request.session.get('role')

    if user_role == 'admin' or user_role == 'role':
      return view_func(request, *args, **kwargs)
    else:
      return HttpResponse('unauthorized')
  
  return wrapper
