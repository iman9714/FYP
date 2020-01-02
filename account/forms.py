from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from account.models import Profile


class VolunteerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' ,'email', 'password1', 'password2')

class EditProfile(UserChangeForm):
    class Meta:
        model = Profile
        fields = [
        'ic',
        'personal_contact'
        ]
        
