from django.urls import path, include
from django.contrib import admin
from . import views 

urlpatterns = [
    path('add_contact', views.add_contact, name='add-contact'),
    path('view_contact', views.view_contact, name='view-contact'),
    path('update_contact/<contact_id>', views.update_contact, name='update-contact'),
    path('remove_contact/<contact_id>', views.remove_contact, name='remove-contact'),
]