from django.db import models
from django.contrib.auth.models import User
import datetime
from profiles.models import Consumer,Moderator
# Create your models here.
'''
    here I've tried to implement a model for tasks that is related to moderator and consumer so 
    a consumer can assign a task to moderator and moderator on completing the task 
'''

class Task(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField()
    deadline    = models.DateField(default=datetime.date.today)
    completion_date = models.DateField(null=True,blank=True)
    consumer = models.ForeignKey(Consumer,related_name="consumer",on_delete=models.CASCADE)
    moderator = models.ForeignKey(Moderator,related_name="moderator",on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.title