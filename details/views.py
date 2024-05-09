from django.shortcuts import render, redirect
from .models import Contact, Experience, Education, Skills
from .forms import ContactForm, ExperienceForm, EducationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def add_contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user.id
            contact.save()
            # form.save()
            return HttpResponseRedirect('/add_contact?submitted=True')
    else: 
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True 
        return render(request, 'details/add_contact.html', {'form': form, 'submitted': submitted})
    
def view_contact(request):
    # contact_list = Contact.objects.filter(owner=request.user.id)
    contact_list = Contact.objects.filter(owner=request.user.id)
    return render(request, 'details/show_contact.html', {'contact_list': contact_list})

def update_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('view-contact')
    return render(request, 'details/update_contact.html', {'form': form, 'contact': contact})

def remove_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    return redirect('view-contact')

def add_experience(request):
    submitted = False
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.owner = request.user.id
            exp.save()
            # form.save()
            return HttpResponseRedirect('/add_experience?submitted=True')
    else: 
        form = ExperienceForm
        if 'submitted' in request.GET:
            submitted = True 
        return render(request, 'details/add_experience.html', {'form': form, 'submitted': submitted})
    
def view_experience(request):
    exp_list = Experience.objects.filter(owner=request.user.id)
    return render(request, 'details/show_experience.html', {'exp_list': exp_list})

def update_experience(request, exp_id):
    exp = Experience.objects.get(pk=exp_id)
    form = ExperienceForm(request.POST or None, instance=exp)
    if form.is_valid():
        form.save()
        return redirect('view-experience')
    return render(request, 'details/update_experience.html', {'form': form, 'experience': exp})

def remove_experience(request, exp_id):
    exp = Experience.objects.get(pk=exp_id)
    exp.delete()
    return redirect('view-experience')

def add_education(request):
    submitted = False
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            educ = form.save(commit=False)
            educ.owner = request.user.id
            educ.save()
            # form.save()
            return HttpResponseRedirect('/add_education?submitted=True')
    else: 
        form = EducationForm
        if 'submitted' in request.GET:
            submitted = True 
        return render(request, 'details/add_education.html', {'form': form, 'submitted': submitted})
    
def view_education(request):
    educ_list = Education.objects.filter(owner=request.user.id)
    return render(request, 'details/show_education.html', {'educ_list': educ_list})

def update_education(request, educ_id):
    educ = Education.objects.get(pk=educ_id)
    form = EducationForm(request.POST or None, instance=educ)
    if form.is_valid():
        form.save()
        return redirect('view-education')
    return render(request, 'details/update_education.html', {'form': form, 'education': educ})

def remove_education(request, educ_id):
    educ = Education.objects.get(pk=educ_id)
    educ.delete()
    return redirect('view-education')