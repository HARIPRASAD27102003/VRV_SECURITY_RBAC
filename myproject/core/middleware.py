from django.http import HttpResponse

EXLUDE_PATH = []

class RoleBaseAccessMiddlware:
  def __init__(self,get_response):
    self.get_response = get_response

  def __call__(self, request):  
    path:str = request.path.strip('/')
    role = request.session.get('role')

    print(role)

    if path.startswith('admin/') and role != 'admin':
      return HttpResponse("unauthorized")

    elif path.startswith('role/') and role != 'role':
      if role == 'admin':
        return self.get_response(request)
      else:
        return HttpResponse("unauthorized")
    
    elif path.startswith('user/') and role != 'user':
      return HttpResponse("You can't access the user's data!")

    return self.get_response(request)