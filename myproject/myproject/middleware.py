from django.http import HttpResponse

class Check_logged_user_middleware:
  def __init__(self,get_response):
    self.get_response = get_response
  
  def __call__(self, request):
    response = self.get_response(request)
    return response