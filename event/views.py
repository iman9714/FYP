from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Event, Activity
from account.models import User,Profile
from FYP.filtering import text_to_vector, get_cosine, eventProfile,filtering
from _operator import attrgetter
from .forms import CreateEvent


# Create your views here.


def event_view(request):
    context = {}
    events = Event.objects.all()
    activity = Activity.objects.all()

    context = {'events':events, 'activity':activity}
    return render(request, "event/home.html", context)


def event_detail(request, id):
    context = {}
    rec_list = []
    rec_id = []
    events = Event.objects.get(pk=id)
    activity = Activity.objects.all()
    users = User.objects.all()
    rec = eventProfile(id)
    for x in rec:
        rec_list.append(filtering(int(x.__dict__['id']),float(x.__dict__['similarity'])))


    rec_list2 = sorted(rec_list, key=attrgetter('similarity'), reverse=True)
    for x in rec_list2:
        print("ID: " + str(x.id) +" Similarity :"+ str(x.similarity))
        if x.similarity > 0.0:
            rec_id.append(x.id)


    context = {'events':events, 'activity':activity, 'rec_id':rec_id, 'users':users}
    return render(request, "event/event_detail.html", context)

def create_event(request):
    if request.POST:
        form = CreateEvent(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event successfully Create!')
            return redirect('home')
        else:
            messages.success(request, 'Error occur')
            context = {'form':form}

    else:
        form = CreateEvent()
        context = {'form':form}

    return render(request, 'event/create_event.html', context)
