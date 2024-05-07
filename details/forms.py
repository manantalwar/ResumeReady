from django import forms 
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact 
        fields = ('phone', 'linkedin', 'website', 'address')
