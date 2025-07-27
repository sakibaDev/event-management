from django import forms
from events.models import Category, Event, Participant

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class EventForm(forms.ModelForm):
    from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'  # Or list your fields explicitly

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input border rounded px-3 py-2 w-full'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-input border rounded px-3 py-2 w-full'
            }),
        }



class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']  
        widgets = {
            'events': forms.CheckboxSelectMultiple  
        }
