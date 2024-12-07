from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from core.models import Permission, Role,User

def api_remove_role(request,role_id):
  session_role = request.session.get('role')

  if session_role != None and (session_role == 'role' or session_role == 'admin'):
    try:
      role = Role.objects.get(pk=role_id)
      role.delete()
      return JsonResponse({'message': 'Role removed successfully'},status=200)
    except Role.DoesNotExist:
      return JsonResponse({'error': 'Role not found'}, status=404)
    except Exception as e:  
      return JsonResponse({'error': 'An error occurred'}, status=500)
  
  return JsonResponse({'error': 'Unauthorized'}, status=400)

def api_remove_role_permission(request,role_id,permission_id):
  session_role = request.session.get('role')

  if session_role != None and (session_role == 'role' or session_role == 'admin'):
    try:
      role = Role.objects.get(pk=role_id)
      permission = role.permissions.get(pk=permission_id)
      permission.delete()
      return JsonResponse({'message': 'Permission removed successfully'},status=200)
    except Role.DoesNotExist:
      return JsonResponse({'error': 'Role not found'}, status=404)
    except Permission.DoesNotExist:
      return JsonResponse({'error': 'Permission not found'}, status=404)
    except Exception as e:  
      return JsonResponse({'error': 'An error occurred'}, status=500)
  
  return JsonResponse({'error': 'Unauthorized'}, status=400)