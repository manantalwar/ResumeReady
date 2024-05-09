from django import forms 
from django.forms import ModelForm
from .models import Contact, Experience, Education, Skills

class ContactForm(ModelForm):
    class Meta:
        model = Contact 
        fields = ('phone', 'linkedin', 'website', 'address')

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ('role', 'company', 'start_date', 'end_date', 'description')

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ('degree', 'major', 'institution', 'start_date', 'end_date', 'coursework', 'gpa')

# class SkillsForm(ModelForm):
#     class Meta:
#         model = Skills
#         fields = ('skills', )