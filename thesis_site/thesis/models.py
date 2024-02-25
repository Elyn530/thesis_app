from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Published(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(ThesisStatus=ThesisList.ThesisStatus.PUBLISHED)

class ThesisList(models.Model):

    class ThesisStatus(models.TextChoices):
        Complete = 'PASSED'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    author = models.CharField (max_length=250)
    department = models.CharField (max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, 
                              choices=ThesisStatus.choices,
                              default=ThesisStatus.Complete)
    objects = models.Manager()
    published = Published()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Thesis_detail", 
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,])

class Comment(models.Model):
    comment = models.ForeignKey(ThesisList, 
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email=models.EmailField()
    body= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.comment}'
