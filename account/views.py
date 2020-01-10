from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import VolunteerRegisterForm,Edit_basic_user
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile,Skill,Cause,NGO,Address,Education,Contact,Experiance


def user_logout(request):
    logout(request)
    messages.success(request, 'Your are successfully Logout!')
    return redirect('login')

@login_required
def account_view_profile(request,  pk=None):
    if not request.user.is_authenticated:
        return redirect('login')

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    profile = Profile.objects.filter(user = user.id)
    skill = Skill.objects.filter(profile = user.profile.id)
    cause = Cause.objects.filter(profile = user.profile.id)
    ngo = NGO.objects.filter(profile = user.profile.id)
    address = Address.objects.filter(profile = user.profile.id)
    education = Education.objects.filter(profile = user.profile.id)
    contact = Contact.objects.filter(profile = user.profile.id)
    experiance = Experiance.objects.filter(profile = user.profile.id)

    context = {'user': user, 'profile':profile, 'skill':skill, 'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}
    return render(request, 'accounts/account_view_profile.html', context)


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


@login_required
def account_edit_profile(request, pk=None):
    if not request.user.is_authenticated:
        return redirect('login')

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    if 'basic' in request.POST:
        form = Edit_basic_user(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your are successfully Updated!')
            return redirect('profile')
            
    else:
        form = Edit_basic_user(instance=request.user)
        context = {'form': form}
        return render(request, 'accounts/account_view_profile.html', context)
