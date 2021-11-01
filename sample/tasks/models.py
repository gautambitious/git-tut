from django.db import models

# Create your models here.
class CustomUser(models.Model):
    username = models.CharField(max_length=200, null = False)
    password = models.CharField(max_length=200, null = False)
    
    def __str__(self):
        return self.username
    
class Task(models.Model):
    task_name = models.CharField(max_length=200, null = False)
    task_completed = models.BooleanField(default=False)
    task_description = models.TextField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    
