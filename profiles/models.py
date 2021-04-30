from django.db import models
from django.contrib.auth.models import User
# Create your models here.


""" 
    here I tried to make two models for each moderator and consumer
    consumer can be seen as how much business he is giving to company by tasks given
    moderators can be ranked on parameters like efficiency and tasks completed
"""


class Moderator(models.Model):
   
    contact_number = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tasks_completed = models.IntegerField()
    efficiency = models.FloatField()


    def __str__(self):
        return "Moderator|"+self.user.username


class Consumer(models.Model):
    contact_number = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tasks_given = models.IntegerField()
    
    def __str__(self):
        return "|Consumer|"+self.user.username