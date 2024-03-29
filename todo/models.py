from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    notes = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
class ChecklistItem(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)