from django.shortcuts import render, redirect
from core.models import Permission, Role, User
from django.contrib import messages 
from.utils import check_logged_user, admin_only,admin_and_role_only
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

@check_logged_user
def sign_page(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username)
      if user.password == password:
        request.session['username'] = user.username
        role = user.roles.name if user.roles else 'no_role'
        request.session['role'] = role
        
        print(role)

        if role == 'admin':
          permissions = user.roles.permissions.all()
          request.session['permissions'] = [permission.name for permission in permissions]
          return redirect('home')
        elif role == 'role_manager':
          permissions = user.roles.permissions.all()
          request.session['permissions'] = [permission.name for permission in permissions]
          return redirect('role_management')
        elif role == 'customer':
          permissions = user.roles.permissions.all()
          request.session['permissions'] = [permission.name for permission in permissions]
          return HttpResponse("Under dev")
        else:
          pass
    except User.DoesNotExist:
      pass

  return render(request,'sign_page/index.html')

def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    role = request.POST.get('role')

    try:
      user = User.objects.get(username=username)

      if user.password.strip() != password.strip():
        print('password is incorrect',user.password, password)
        messages.error(request,'Password incorrect')
        return HttpResponse('password is wrong')
      
      user_role = user.roles.name
      print(user_role)

      if user_role.lower() == 'admin' and role == 'admin':
        request.session['first_name'] = user.first_name
        request.session['username'] = user.username
        request.session['role'] = user_role.lower()
        request.session['permissions'] = [permissions.name for permissions in user.roles.permissions.all()]

        return redirect("home")
      
      elif user_role.lower() == 'role' and role ==  'role':
        request.session['first_name'] = user.first_name
        request.session['username'] = user.username
        request.session['role'] = user_role.lower()
        request.session['permissions'] = ','.join(permission.name for permission in user.roles.permissions.all())
        
        return redirect("role_management")
      
      elif user_role.lower() == 'user' and role is 'user':
        return HttpResponse('This is user')

      else:
        return HttpResponse('Unauthorized Access. Please contact your administrator.')
    
    except User.DoesNotExist:
      return HttpResponse("user doesnt exist")
    
  return HttpResponse('This is not working as expected')

def create_user_page(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    re_password = request.POST.get('re_enter_password')

    return redirect('create_user_page')

  return render(request,'sign_page/create_user.html')

# @admin_only
def home(request):
  total_user = len(User.objects.all())
  total_role = len(Role.objects.all())
  total_permission = len(Permission.objects.all())

  data = {
    "total_user" : total_user,
    "total_role" : total_role,
    "total_permission" : total_permission,
  }

  return render(request,'home/home.html',data)

# @admin_only
@admin_and_role_only
def role_management(request):
  roles = Role.objects.all()
  q = request.GET.get('q','')

  if q:
    roles = Role.objects.all().filter(name__icontains=q)

  return render(request,'role/role.html',{ "roles" : roles,"q":q })

def user_management(request):
  return render(request,'home/user.html')

def add_role(request):
  permisions = Permission.objects.all()

  if request.method == "POST":
    role_name = request.POST.get("role_name")
    role_desc = request.POST.get("role_desc")
    seleted_permission_ids = request.POST.getlist('permission_list')

    selected_permission = Permission.objects.filter(pk__in=seleted_permission_ids)
    if len(selected_permission) != len(seleted_permission_ids):
      return HttpResponseBadRequest("Selected permissions do no exist!")

    new_role = Role.objects.create(name = role_name, description = role_desc)
    new_role.permissions.add(*selected_permission)
    
    return HttpResponseRedirect("/roles/success")

  return render(request,'role/add_role.html' , {"permissions" : permisions})

def remove_role(request):
  roles = Role.objects.prefetch_related("permissions")
  q = request.GET.get('q','')

  if q:
    roles = Role.objects.all().filter(name__icontains=q)

  return render(request,'role/remove_role.html',{"roles" : roles})

def edit_role(request):
  roles = Role.objects.prefetch_related("permissions")
  q = request.GET.get('q','')

  if q:
    roles = Role.objects.all().filter(name__icontains=q)
  
  return render(request,'role/edit_role.html',{"roles" : roles})

def edit_role_id(request, pk):
  roles = Role.objects.prefetch_related('permissions').get(pk=pk)

  data = {
    "id" : pk,
    "roles" : roles
  }

  return render(request,'role/edit_role_id.html', data)

def detail_role(request,pk):
  roles = Role.objects.get(pk=pk)

  data = {
    "id" : pk,
    "roles" : roles
  }

  return render(request,"role/detail_role.html",data)

def permission_management(request):
  return render(request, 'permission/permission.html')
  
def detail_permission(request):
  return render(request, 'permission/detail_permission.html')

def add_permission(request):
  return render(request, 'permission/add_permission.html')
def edit_permission(request):
  return render(request, 'permission/edit_permission.html')
def remove_permission(request):
  return render(request, 'permission/remove_permission.html')

def logout(request):
  request.session.flush()
  return redirect('sign_page')

