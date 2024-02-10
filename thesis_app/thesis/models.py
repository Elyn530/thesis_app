from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Thesislist(models.model):
    
    Title = models.CharField(max_length=250)
    Abstract = models.TextField()
    Approval = models.CharField(max_length=250)
    Author = models.CharField(max_length=250)
    Department = models.CharField(max_length=100)
    Adviser = models.CharField(max_length=100)
    Publish = models.DateTimeField(auto_now_add=True)
    
    search = models.TextField(User, )
    
    def __str__(self):
        return self.title