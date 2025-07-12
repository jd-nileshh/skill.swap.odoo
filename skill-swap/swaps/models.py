from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class SwapUser(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.EmailField(unique=True, null=False, primary_key=True)
    city = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='photos', null=False)
    skills = models.TextField()
    skills_wanted = models.TextField()
    is_public = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

class request_swap(models.Model):
    swapuser=models.ForeignKey(SwapUser,on_delete='cascade')
    skill_offered=models.TextField()
    skill_learn=models.TextField()
    message=models.TextField()
    
