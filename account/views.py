from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import VolunteerRegisterForm,Edit_basic_user,Edit_basic_profile,Edit_basic_contact,Edit_address,Add_skill,Add_cause,Add_NGO,Add_education, Add_experiance
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

    return render(request, 'registration/account_register.html', context)

#-------------------------------------------------------------------------------------------------------------------------------
@login_required
def account_management(request, pk=None):
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
        form_user = Edit_basic_user(request.POST or None, instance=user)
        form_profile = Edit_basic_profile(request.POST or None,request.FILES, instance=profile.first())
        form_contact = Edit_basic_contact(request.POST or None, instance=contact.first())

        if form_user.is_valid() and form_profile.is_valid() and form_contact.is_valid():
            instance = form_user.save(commit=False)
            instance2 = form_profile.save(commit=False)
            instance3 = form_contact.save(commit=False)

            instance.user = user
            instance2.profile = Profile.objects.filter(user = user.id).first()
            instance3.profile = Profile.objects.filter(user = user.id).first()

            instance.save()
            instance2.save()
            instance3.save()
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
        form_address = Edit_address(request.POST or None, instance=address.first())
        if form_address.is_valid():
            instance = form_address.save(commit=False)
            instance.profile = Profile.objects.filter(user = user.id).first()
            instance.save()
            messages.success(request, 'Your Address successfully Updated!')
            return redirect('profile')

    else:
        form_address= Edit_address(instance=address.first())
        context = {'form_address': form_address,'user': user, 'profile':profile, 'skill':skill,
        'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}

    #add skill
    add_skill_form = Add_skill(request.POST)
    if 'add-skill' in request.POST:
        if add_skill_form.is_valid():
            instance = add_skill_form.save(commit=False)
            instance.profile = Profile.objects.filter(user = user.id).first()
            instance.save()
            messages.success(request, 'Skill successfully Added!')
            return redirect('profile')
        else:
            context = {'add_skill_form':add_skill_form,'form_address': form_address,'user': user, 'profile':profile, 'skill':skill,
            'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}

    #add cause
    add_cause_form = Add_cause(request.POST)
    if 'add-cause' in request.POST:
        if add_cause_form.is_valid():
            instance = add_cause_form.save(commit=False)
            instance.profile = Profile.objects.filter(user = user.id).first()
            instance.save()
            messages.success(request, 'Cause successfully Added!')
            return redirect('profile')
        else:
            context = {'add_cause_form':add_cause_form,'add_skill_form':add_skill_form,'form_address': form_address,'user': user, 'profile':profile, 'skill':skill,
            'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}


    #add NGO
    add_ngo_form = Add_NGO(request.POST)
    if 'add-ngo' in request.POST:
        if add_ngo_form.is_valid():
            instance = add_ngo_form.save(commit=False)
            instance.profile = Profile.objects.filter(user = user.id).first()
            instance.save()
            messages.success(request, 'NGO successfully Added!')
            return redirect('profile')
        else:
            context = {'add_ngo_form':add_ngo_form, 'add_cause_form':add_cause_form,'add_skill_form':add_skill_form,'form_address': form_address,'user': user, 'profile':profile, 'skill':skill,
            'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}

    #add Education
    add_education_form = Add_education(request.POST)
    if 'add-education' in request.POST:
        if add_education_form.is_valid():
            instance = add_education_form.save(commit=False)
            instance.profile = Profile.objects.filter(user = user.id).first()
            instance.save()
            messages.success(request, 'Education successfully Added!')
            return redirect('profile')
        else:
            context = {'add_education_form':add_education_form, 'add_ngo_form':add_ngo_form, 'add_cause_form':add_cause_form,'add_skill_form':add_skill_form,'form_address': form_address,'user': user, 'profile':profile, 'skill':skill,
            'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}


    add_experiance_form = Add_experiance(request.POST)
    if 'add-experiance' in request.POST:
        if add_experiance_form.is_valid():
            instance = add_experiance_form.save(commit=False)
            instance.profile = Profile.objects.filter(user = user.id).first()
            instance.save()
            messages.success(request, 'Experiance successfully Added!')
            return redirect('profile')
        else:
            context = {'add_experiance_form':add_experiance_form, 'add_education_form':add_education_form, 'add_ngo_form':add_ngo_form, 'add_cause_form':add_cause_form,'add_skill_form':add_skill_form,'form_address': form_address,'user': user, 'profile':profile, 'skill':skill,
            'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}

    context = {'add_experiance_form':add_experiance_form,'add_education_form':add_education_form, 'add_ngo_form':add_ngo_form,'add_cause_form':add_cause_form,'add_skill_form':add_skill_form,'form_user': form_user,'form_profile': form_profile, 'form_contact': form_contact,'form_address': form_address, 'user': user, 'profile':profile, 'skill':skill,
    'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}
    return render(request, 'accounts/account_view_profile.html', context)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
