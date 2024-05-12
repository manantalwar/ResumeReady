from django.shortcuts import render
from details.models import Contact, Experience, Education, Skills
from django.contrib.auth.models import User

def test_view(request):
    # Fetch data from models
    contacts = Contact.objects.filter(owner=request.user.id)[0]
    experiences = Experience.objects.filter(owner=request.user.id).order_by('-start_date')
    education = Education.objects.filter(owner=request.user.id).order_by('-start_date')
    sk = Skills.objects.filter(owner=request.user.id)
    return render(request, 'pdfgen/resume.html', {'contacts': contacts, 'experiences': experiences, 'education': education, 'sk':sk})
