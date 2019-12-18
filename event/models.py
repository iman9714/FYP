from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    #admin              = models.OneToManyField(User, on_delete=models.CASCADE, primary_key=True)
    title               = models.CharField(max_length=60)
    start_date          = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=False)
    end_date            = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    start_time          = models.TimeField(auto_now_add=False, auto_now=False, blank=True, null=False)
    end_time            = models.TimeField(auto_now_add=False, auto_now=False, blank=True, null=False)
    location            = models.TextField(null=False)


    class Meta:
        verbose_name_plural = 'Event'

    def __str__(self):
        return self.title


class Activity(models.Model):
    event               = models.ForeignKey(Event,on_delete=models.CASCADE,null=True, related_name='activity')
    #volunteer          = models.ManyToManyField(User, on_delete=models.CASCADE, primary_key=True)
    title               = models.CharField(max_length=60)
    category            = models.CharField(max_length=200)#multivelue
    description         = models.TextField(max_length=300, blank=True)
    collaboration       = models.CharField(max_length=100, blank=True)#multivelue

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Activity'


class Logistic(models.Model):
    #volunteer           = models.OneToManyField(User, on_delete=models.CASCADE, primary_key=True)
    activity             = models.OneToOneField(Activity, on_delete=models.CASCADE, primary_key=True)
    task                 = models.CharField(max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Logistic'
