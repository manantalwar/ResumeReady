from django import forms 
from django.forms import ModelForm
from .models import Contact, Experience, Education, Skills, Jobs

class ContactForm(ModelForm):
    class Meta:
        model = Contact 
        fields = ('phone', 'linkedin', 'website', 'address')
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['linkedin'].widget.attrs['class'] = 'form-control'
        self.fields['website'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ('role', 'company', 'start_date', 'end_date', 'description')

    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ('degree', 'major', 'institution', 'start_date', 'end_date', 'coursework', 'gpa')
    
    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['degree'].widget.attrs['class'] = 'form-control'
        self.fields['major'].widget.attrs['class'] = 'form-control'
        self.fields['institution'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.fields['coursework'].widget.attrs['class'] = 'form-control'
        self.fields['gpa'].widget.attrs['class'] = 'form-control'

class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = ('skills', )
    
    def __init__(self, *args, **kwargs):
        super(SkillsForm, self).__init__(*args, **kwargs)
        self.fields['skills'].widget.attrs['class'] = 'form-control'


class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        fields = ('description', 'qualifications')
    
    def __init__(self, *args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['qualifications'].widget.attrs['class'] = 'form-control'

