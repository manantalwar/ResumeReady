from django.urls import path, include
from django.contrib import admin
from . import views 

urlpatterns = [
    path('create_pdf', views.create_pdf, name='create-pdf'),
]
