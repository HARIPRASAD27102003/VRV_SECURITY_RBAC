from django.db import models

class Permission(models.Model):
  name = models.CharField(max_length=100,unique=True)
  description = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name
  
class Role(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(blank=True, null=True)
  permissions = models.ManyToManyField(Permission, related_name='roles', blank=True)

  def __str__(self):
    return self.name

class User(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  username = models.CharField(max_length=100,unique=True)
  password = models.CharField(max_length=100,null=True,blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  roles = models.ForeignKey(Role,related_name='users',blank=True,null=True,on_delete=models.CASCADE)

  def __str__(self):
    return self.username