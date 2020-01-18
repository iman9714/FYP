from django.shortcuts import render, redirect,get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Event, Activity,Logistic
from account.models import Profile,Skill,Cause,NGO,Address,Education,Contact,Experiance
from FYP.filtering import text_to_vector, get_cosine, eventProfile,filtering,event_recommender
from _operator import attrgetter
from django.contrib import messages
from .forms import CreateEvent,add_activity, add_logistic, EditEvent





#--------list of event class-------------------------------------------------------
def event_view(request):
    context = {}
    events = Event.objects.all()
    activity = Activity.objects.all()
    form = CreateEvent(request.POST or None)

    context = {'events':events, 'activity':activity,'form':form}
    return render(request, "event/event_list.html", context)

#--------list of Suggested event for volunteer class-------------------------------------------------------
def recommended_event(request):
    context = {}
    rec_list = []
    rec_id = []
    events = Event.objects.all()
    rec_event = event_recommender(request.user.id)

    for x in rec_event:
        rec_list.append(filtering(int(x.__dict__['id']),float(x.__dict__['similarity'])))

    rec_list2 = sorted(rec_list, key=attrgetter('similarity'), reverse=True)
    for x in rec_list2:
        print("ID: " + str(x.id) +" Similarity :"+ str(x.similarity))
        rec_id.append(x.id)

    joined_event =  request.user.event_set.all()

    context = {'rec_id':rec_id,'events':events,'joined_event':joined_event}
    return render(request, "event/home.html", context)

#--------Event detail class-------------------------------------------------------
def event_management(request, id):
    context = {}
    rec_list = []
    rec_id = []

    events = Event.objects.get(pk=id)
    activity = Activity.objects.filter(event = events.id)
    logistic = Logistic.objects.filter(event = events.id)
    users = User.objects.all()
    rec = eventProfile(id)


#--------Matching Technique class Filtering--
    for x in rec:
        rec_list.append(filtering(int(x.__dict__['id']),float(x.__dict__['similarity'])))

    rec_list2 = sorted(rec_list, key=attrgetter('similarity'), reverse=True)
    for x in rec_list2:
        print("ID: " + str(x.id) +" Similarity :"+ str(x.similarity))
        rec_id.append(x.id)


#--------add activity---------
    activity_form = add_activity(request.POST)
    if 'add_activity' in request.POST:
        if activity_form.is_valid():
            instance = activity_form.save(commit=False)
            instance.event = events
            instance.save()
            messages.success(request, 'Activity successfully Create!')
            return redirect('detail', id=id)
        else:
            context = {'events':events, 'activity':activity, 'rec_id':rec_id, 'users':users,'logistic':logistic,'activity_form':activity_form}
            return redirect('detail',id=id)

#--------add logistic---------------------
    logistic_form = add_logistic(request.POST)
    if 'add_logistic' in request.POST:
        if logistic_form.is_valid():
            instance = logistic_form.save(commit=False)
            instance.event = events
            instance.save()
            logistic_form.save_m2m()
            messages.success(request, 'Logistic successfully Added!')
            return redirect('detail', id=id)
        else:
            context = {'events':events, 'activity':activity, 'rec_id':rec_id, 'users':users,'logistic':logistic,'activity_form':activity_form,'logistic_form':logistic_form}
            return redirect('detail',id=id)

#--------Join Event------------------
    if 'join-event' in request.POST:
        events = Event.objects.get(pk=id)
        Event.join(request.user,events)
        messages.success(request, 'You are successfully Added to the Volunteers List!')

        context = {'events':events, 'activity':activity, 'rec_id':rec_id, 'users':users,'logistic':logistic,'activity_form':activity_form,'logistic_form':logistic_form}
        return redirect('detail',id=id)

#--------Unjoin Event----------------------
    if 'unjoin-event' in request.POST:
        events = Event.objects.get(pk=id)
        Event.unjoin(request.user,events)
        messages.success(request, 'You are successfully Remove from the Volunteers List!')

        context = {'events':events, 'activity':activity, 'rec_id':rec_id, 'users':users,'logistic':logistic,'activity_form':activity_form,'logistic_form':logistic_form}
        return redirect('detail',id=id)

#--------Edit event---------------------
    event_edit = EditEvent(request.POST or None ,instance=events)
    if 'edit-event' in request.POST:
        if event_edit.is_valid():
            event_edit.save()
            messages.success(request, 'Event is successfully Updated!')
            return redirect('detail', id=id)
        else:
            context = {'events':events, 'activity':activity, 'rec_id':rec_id, 'users':users,'logistic':logistic,'activity_form':activity_form,'event_edit':event_edit}
            return redirect('detail',id=id)

#--------Delete event------------
    if 'delete-event' in request.POST:
        events.delete()
        messages.success(request, 'Event is successfully Deleted!')
        return redirect('event_view')

    current_event = None
    if request.user.is_authenticated:
        current_event  = request.user.event_set.filter(pk=id)


    context = {'current_event':current_event,'events':events, 'activity':activity, 'rec_id':rec_id, 'users':users,'logistic':logistic,'activity_form':activity_form,'logistic_form':logistic_form,'event_edit':event_edit}
    return render(request, "event/event_detail.html", context)


#--------create Event class-------------------------------------------------------
def create_event(request):
    if 'create_event' in request.POST:
        form = CreateEvent(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event successfully Create!')
            return redirect('event_view')
        else:
            #messages.success(request, 'Error occur')
            context = {'form':form}
            return redirect('event_view')
    else:
        form = CreateEvent()
        context = {'form':form}

    return render(request, 'event/event_list.html', context)

#--------View Volunteer Detail class-------------------------------------------------------
def view_volunteer_detail(request, volunteer_id):
    users = User.objects.get(pk=volunteer_id)
    profile = Profile.objects.filter(user = users.id)
    skill = Skill.objects.all().filter(profile = users.profile.id)
    cause = Cause.objects.filter(profile = users.profile.id)
    ngo = NGO.objects.filter(profile = users.profile.id)
    address = Address.objects.filter(profile = users.profile.id)
    education = Education.objects.filter(profile = users.profile.id)
    contact = Contact.objects.filter(profile = users.profile.id)
    experiance = Experiance.objects.filter(profile = users.profile.id)

    context = { 'users': users, 'profile':profile, 'skill':skill,'cause':cause, 'ngo':ngo, 'address':address,'education':education, 'contact':contact, 'experiance':experiance}
    return render(request, 'event/view_volunteer_detail.html', context)
