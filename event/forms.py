from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from event.models import Event, Activity, Logistic

class CreateEvent(ModelForm):
    class Meta:
        model = Event
        fields = ('title','start_date','end_date','start_time','end_time','location')


class add_activity(ModelForm):
    class Meta:
        model = Activity
        fields = ['title','category','description','collaboration']

class add_logistic(ModelForm):
    user_id = forms.ChoiceField(choices=[(x.id, x.first_name+' '+x.last_name) for x in User.objects.all()])
    class Meta:
        model = Logistic
        exclude = ['event']
