from django.urls import path, include
from django.contrib import admin
from . import views 

urlpatterns = [
    path('add_contact', views.add_contact, name='add-contact'),
    path('view_contact', views.view_contact, name='view-contact'),
    path('update_contact/<contact_id>', views.update_contact, name='update-contact'),
    path('remove_contact/<contact_id>', views.remove_contact, name='remove-contact'),
    path('add_experience', views.add_experience, name='add-experience'),
    path('view_experience', views.view_experience, name='view-experience'),
    path('update_experience/<exp_id>', views.update_experience, name='update-experience'),
    path('remove_experience/<exp_id>', views.remove_experience, name='remove-experience'),
    path('add_education', views.add_education, name='add-education'),
    path('view_education', views.view_education, name='view-education'),
    path('update_education/<educ_id>', views.update_education, name='update-education'),
    path('remove_education/<educ_id>', views.remove_education, name='remove-education'),
    path('add_skills', views.add_skills, name='add-skills'),
    path('view_skills', views.view_skills, name='view-skills'),
    path('update_skills/<skill_id>', views.update_skills, name='update-skills'),
    path('remove_skills/<skill_id>', views.remove_skills, name='remove-skills'),
    path('home', views.view_home, name='home'),
    path('add_job', views.add_job, name='add-job'),
    path('view_jobs', views.view_jobs, name='view-jobs'),
    path('remove_jobs/<job_id>', views.remove_jobs, name='remove-jobs'),
    path('update_jobs/<job_id>', views.update_jobs, name='update-jobs'),
]