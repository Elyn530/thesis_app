from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Thesismodel(models.model):
    
    Title = models.CharField(max_length=250)
    Abstract = models.TextField()
    Approval = models.TextField()
    Author = models.CharField(max_length=250)
    Department = models.CharField(max_length=100)
    Adviser = models.CharField(max_length=100)
    Publish = models.DateTimeField()
    
    search = models.TextField(User, )
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]
         