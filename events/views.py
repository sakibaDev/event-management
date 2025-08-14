from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from events.models import Event,Category,Participant
from .forms import EventForm, ParticipantForm, CategoryForm



# Create your views here.



from datetime import date

def dashboard(request):
    today = date.today()

    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(date__gt=today).count()
    past_events = Event.objects.filter(date__lt=today).count()
    total_participants = Participant.objects.count()

    todays_events = Event.objects.filter(date=today)

    return render(request, "dashboard/dashboard.html", {
        "total_events": total_events,
        "upcoming_events": upcoming_events,
        "past_events": past_events,
        "total_participants": total_participants,
        "todays_events": todays_events
    })


# ------Event Views------


def event_list(request):
    category_id = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    events = Event.objects.select_related('category').prefetch_related('participants')

    if category_id:
        events = events.filter(category__id=category_id)

    if start_date and end_date:
        events = events.filter(date__range=[start_date, end_date])

    total_participants = Participant.objects.count()

    categories = Category.objects.all() 

    return render(request, 'events/event_list.html', {
        'events': events,
        'total_participants': total_participants,
        'categories': categories
    })

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
        
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})



def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')


# ----Category Views----

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})
                              

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  
    else:
        form = CategoryForm()
    return render(request, 'category/category_form.html', {'form': form})


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('category_list')

# ----Participant Views----

def  participant_list(request):

    participants = Participant.objects.all()
    return render(request, 'participant/participant_list.html', {'participants': participants})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list') 
    else:
        form = ParticipantForm()
    return render(request, 'participant/participant_form.html', {'form': form})


def participant_update(request, pk):
    participants = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participants)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participants)
    return render(request, 'participant/participant_form.html', {'form': form})


def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    participant.delete()
    return redirect('participant_list')