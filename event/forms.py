from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from event.models import Event

class CreateEvent(ModelForm):
    class Meta:
        model = Event
        fields = ('title','start_date','end_date','start_time','end_time','location')
