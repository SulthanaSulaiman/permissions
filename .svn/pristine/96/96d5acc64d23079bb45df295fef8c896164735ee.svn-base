from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=150, unique=True)
    publisher_address = models.CharField(max_length=250, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now_add=True)
    publisher_logo = models.ImageField(upload_to='logos', null=True)
    publisher_imprint = models.CharField(max_length=250, blank=True, null=True)
   
    def __str__(self):
        return self.publisher_name