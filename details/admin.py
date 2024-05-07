from django.contrib import admin
from .models import Contact, Experience, Education, Skills, ResumeUser

# Register your models here.
admin.site.register(Contact)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(ResumeUser)