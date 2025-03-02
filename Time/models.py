from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id_device = models.UUIDField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TimeEntry(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='time_entries')
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project.title} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"


