from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from account.models import Profile, Contact, Address, Skill

class VolunteerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' ,'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % user)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)

class Add_skill(ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']

class Edit_basic_profile(ModelForm):
    class Meta:
        model = Profile
        fields = ['occupation']

class Edit_basic_user(ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % user)

class Edit_basic_contact(ModelForm):
    class Meta:
        model = Contact
        fields = ['office_contact','personal_contact']

class Edit_address(UserChangeForm):
    class Meta:
        model = Address
        fields = ['address','zip_code','state', 'country', 'office_address', 'office_zip_code', 'office_state', 'office_country' ]

class Edit_skill(ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']
