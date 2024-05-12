from django.contrib import admin
from django.urls import path, include
from authentication.views import user_login
from . import views

urlpatterns = [
    path('view_res/<job_id>', views.test, name='view-res'),
]