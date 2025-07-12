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
    sender = models.ForeignKey(SwapUser, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(SwapUser, on_delete=models.CASCADE, related_name='received_requests')
    skill_offered = models.TextField()
    skill_learn = models.TextField()
    message = models.TextField()
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    timestamp = models.DateTimeField(auto_now_add=True)
    
