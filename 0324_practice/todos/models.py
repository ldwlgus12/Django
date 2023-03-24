from django.db import models

# Create your models here.

class Todo(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    dead_line = models.DateTimeField(null=True)
    category = models.CharField(max_length=20, blank=True)
