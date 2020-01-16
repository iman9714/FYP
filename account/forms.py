from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from account.models import Profile, Contact, Address, Skill,Cause, NGO, Education, Experiance

#--------------------------------------------Add section---------------------------------------------------------------------------
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

class Add_cause(ModelForm):
    class Meta:
        model = Cause
        fields = ['cause']

class Add_NGO(ModelForm):
    class Meta:
        model = NGO
        fields = ['name']

class Add_education(ModelForm):
    class Meta:
        model = Education
        fields = ['level','description']

class Add_experiance(ModelForm):
    class Meta:
        model = Experiance
        fields = ['detail']
#--------------------------------------------Edit section---------------------------------------------------------------------------
class Edit_basic_profile(ModelForm):
    class Meta:
        model = Profile
        fields = ['occupation','picture']

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
