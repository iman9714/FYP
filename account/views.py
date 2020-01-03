from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import VolunteerRegisterForm,EditProfile
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


def user_logout(request):
    logout(request)
    messages.success(request, 'Your are successfully Logout!')
    return redirect('login')

@login_required
def account_view_profile(request):
    template_name = 'accounts/profile.html'
    user = request.user
    context = {'form':user}
    return render(request, template_name, context)



def account_register(request):
    if request.POST:
        form = VolunteerRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your are successfully registred!')
            return redirect('register')

    else:
        form = VolunteerRegisterForm()
        context = {'form':form}

    return render(request, 'registration/register.html', context)


@login_required
def account_edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}
    if request.POST:
        form = EditProfile(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.initial = {
                "ic": request.POST['ic'],
                "personal_contact": request.POST['personal_contact'],
			}
            form.save()
            context['success_message'] = "Updated"
    else:
        form = EditProfile(
        initial={
            "ic": request.user.profile.ic,
            "personal_contact": request.user.profile.personal_contact,
            })

    context['form'] = form
    return render(request, 'accounts/edit_profile.html', context)
