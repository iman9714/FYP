from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import VolunteerRegisterForm,Edit_basic_user,Edit_basic_profile,Edit_basic_contact,Edit_address,Add_skill
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile,Skill,Cause,NGO,Address,Education,Contact,Experiance

#-------------------------------------------------------------------------------------------------------------------------------
def user_logout(request):
    logout(request)
    messages.success(request, 'Your are successfully Logout!')
    return redirect('login')

#-------------------------------------------------------------------------------------------------------------------------------
def account_register(request):
    context = {}
    if request.POST:
        form = VolunteerRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            messages.success(request, 'Your are successfully registred!')
            return redirect('login')
        else:
            context['form'] = form

    else:
        form = VolunteerRegisterForm()
        context = {'form':form}

    return render(request, 'registration/register.html', context)

#-------------------------------------------------------------------------------------------------------------------------------
@login_required
def account_view_profile(request, pk=None):
    if not request.user.is_authenticated:
        return redirect('login')

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    profile = Profile.objects.filter(user = user.id)
    skill = Skill.objects.all().filter(profile = user.profile.id)
    cause = Cause.objects.filter(profile = user.profile.id)
    ngo = NGO.objects.filter(profile = user.profile.id)
    address = Address.objects.filter(profile = user.profile.id)
    education = Education.objects.filter(profile = user.profile.id)
    contact = Contact.objects.filter(profile = user.profile.id)
    experiance = Experiance.objects.filter(profile = user.profile.id)

    #edit basic information
    if 'basic' in request.POST:
        form_user = Edit_basic_user(request.POST , instance=user)
        form_profile = Edit_basic_profile(request.POST , instance=profile.first())
        form_contact = Edit_basic_contact(request.POST , instance=contact.first())

        if form_user.is_valid() and form_profile.is_valid() and form_contact.is_valid():
            form_user.save()
            form_profile.save()
            form_contact.save()
            messages.success(request, 'Your are successfully Updated!')
            return redirect('profile')

    else:
        form_user = Edit_basic_user(instance=user)
        form_profile = Edit_basic_profile(instance=profile.first())
        form_contact = Edit_basic_contact(instance=contact.first())
        context = {'form_user': form_user,'form_profile': form_profile, 'form_contact': form_contact, 'user': user, 'profile':profile, 'skill':skill,
        'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}

    #edit address
    if 'addressinfo' in request.POST:
        form_address = Edit_address(request.POST , instance=address.first())

        if form_address.is_valid() :
            form_address.save()
            messages.success(request, 'Your Address successfully Updated!')
            return redirect('profile')

    else:
        form_address= Edit_address(instance=address.first())
        context = {'form_address': form_address,'user': user, 'profile':profile, 'skill':skill,
        'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}

    #edit skill



    context = {'form_user': form_user,'form_profile': form_profile, 'form_contact': form_contact,'form_address': form_address, 'user': user, 'profile':profile, 'skill':skill,
    'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}
    return render(request, 'accounts/account_view_profile.html', context)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
