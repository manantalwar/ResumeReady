from django import forms 
from django.forms import ModelForm
from .models import Contact
from .models import Experience

class ContactForm(ModelForm):
    class Meta:
        model = Contact 
        fields = ('phone', 'linkedin', 'website', 'address')

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ('role', 'company', 'start_date', 'end_date', 'description')
        
    
