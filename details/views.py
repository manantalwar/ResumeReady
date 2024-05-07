from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
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
    







