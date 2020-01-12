from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Event(models.Model):
    title               = models.CharField(max_length=128,blank=True)
    start_date          = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    end_date            = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    start_time          = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    end_time            = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    location            = models.TextField(max_length=128,blank=True)
    user_id             = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title+' '+self.location

class Activity(models.Model):
    event               = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='activity')
    title               = models.CharField(max_length=128,blank=True)
    category            = models.CharField(max_length=128,blank=True)
    description         = models.TextField(max_length=128, blank=True)
    collaboration       = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.title+' '+self.category+' '+self.description+' '+self.collaboration


class Logistic(models.Model):
    event               = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='logistic')
    task                = models.CharField(max_length=128,blank=True)
    user_id             = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.task
