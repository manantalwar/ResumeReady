from django.shortcuts import render, redirect
from .models import Contact, Experience, Education, Skills, Jobs
from .forms import ContactForm, ExperienceForm, EducationForm, SkillsForm, JobsForm
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
            return HttpResponseRedirect('/add_contact?submitted=True')
    else: 
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True 
        return render(request, 'details/add_contact.html', {'form': form, 'submitted': submitted})
    
def view_contact(request):
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

def add_skills(request):
    submitted = False
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            skills = form.save(commit=False)
            skills.owner = request.user.id
            skills.save()
            return HttpResponseRedirect('/add_skills?submitted=True')
    else: 
        form = SkillsForm
        if 'submitted' in request.GET:
            submitted = True 
        return render(request, 'details/add_skills.html', {'form': form, 'submitted': submitted})
    
def view_skills(request):
    skills_list = Skills.objects.filter(owner=request.user.id)
    return render(request, 'details/show_skills.html', {'skills_list': skills_list})

def update_skills(request, skill_id):
    skill = Skills.objects.get(pk=skill_id)
    form = SkillsForm(request.POST or None, instance=skill)
    if form.is_valid():
        form.save()
        return redirect('view-skills')
    return render(request, 'details/update_skills.html', {'form': form, 'skill': skill})

def remove_skills(request, skill_id):
    skill = Skills.objects.get(pk=skill_id)
    skill.delete()
    return redirect('view-skills')

def view_home(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    contact_list = Contact.objects.filter(owner=request.user.id)[0]
    skills_list = Skills.objects.filter(owner=request.user.id)
    skills = [elem.skills for elem in skills_list]
    skills = [elem.split(',') for elem in skills]
    skills = [elem.strip() for sublist in skills for elem in sublist]
    educ_list = Education.objects.filter(owner=request.user.id)
    exp_list = Experience.objects.filter(owner=request.user.id)
    jobs_list = Jobs.objects.filter(owner=request.user.id)
    return render(request, 'details/home.html', {'first_name':first_name, 'last_name':last_name,'contact':contact_list, 'skills':skills, 'educ_list':educ_list, 'exp_list': exp_list, 'jobs_list':jobs_list})

def add_job(request):
    submitted = False
    if request.method == "POST":
        form = JobsForm(request.POST)
        if form.is_valid():
            skills = form.save(commit=False)
            skills.owner = request.user.id
            skills.save()
            return HttpResponseRedirect('/add_job?submitted=True')
    else: 
        form = JobsForm
        if 'submitted' in request.GET:
            submitted = True 
        return render(request, 'details/add_job.html', {'form': form, 'submitted': submitted})
    
def view_jobs(request):
    jobs_list = Jobs.objects.filter(owner=request.user.id)
    return render(request, 'details/show_jobs.html', {'jobs_list': jobs_list})

def remove_jobs(request, job_id):
    job = Jobs.objects.get(pk=job_id)
    job.delete()
    return redirect('view-jobs')

def update_jobs(request, job_id):
    job = Jobs.objects.get(pk=job_id)
    form = JobsForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('view-jobs')
    return render(request, 'details/update_jobs.html', {'form': form, 'job': job})
