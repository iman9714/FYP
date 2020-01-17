from django import forms
from django.forms.formsets import formset_factory
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from event.models import Event, Activity, Logistic
from bootstrap_datepicker_plus import DatePickerInput,TimePickerInput



class CreateEvent(ModelForm):
    class Meta:
        model = Event
        fields = ('title','start_date','end_date','start_time','end_time','location')
        widgets = {
            'start_date':DatePickerInput().start_of('event days'),
            'end_date':DatePickerInput().end_of('event days'),
            'start_time':TimePickerInput().start_of('party time'),
            'end_time':TimePickerInput().end_of('party time'),
        }


class EditEvent(ModelForm):
    class Meta:
        model = Event
        fields = ('title','start_date','end_date','start_time','end_time','location')
        widgets = {
            'start_date':DatePickerInput(),
            'end_date':DatePickerInput(),
            'start_time':TimePickerInput(),
            'end_time':TimePickerInput(),
        }

class add_activity(ModelForm):
    class Meta:
        model = Activity
        fields = ['title','category','description','collaboration']

class add_logistic(ModelForm):
    #user_id = forms.ChoiceField(choices=[(x.id, x.first_name+' '+x.last_name) for x in User.objects.all()])
    class Meta:
        model = Logistic
        exclude = ['event']
