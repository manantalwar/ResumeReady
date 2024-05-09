from django.urls import path, include
from django.contrib import admin
from . import views 

urlpatterns = [
    path('create_pdf', views.test_view, name='create-pdf'),
]
