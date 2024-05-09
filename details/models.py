from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    phone = models.CharField('Phone', max_length=10)
    linkedin = models.URLField('LinkedIn')
    website = models.URLField('Website')
    address = models.CharField('Address', max_length=200)
    owner = models.IntegerField('Contact Owner', blank=False, default=1)

    def __str__(self) -> str:
        return self.phone

    
class Experience(models.Model):
    role = models.CharField('Role', max_length=30)
    company = models.CharField('Company', max_length=30)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    description = models.TextField(blank=True)
    owner = models.IntegerField('Experience Owner', blank=False, default=1)

    def __str__(self) -> str:
        return self.role

class Education(models.Model):
    degree = models.CharField('Degree', max_length=30)
    major = models.CharField('Major', max_length=30)
    institution = models.CharField('Institution', max_length=30)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    coursework = models.TextField(blank=True)
    gpa = models.FloatField('GPA')
    owner = models.IntegerField('Education Owner', blank=False, default=1)

    def __str__(self) -> str:
        return self.degree

class Skills(models.Model):
    skills = models.CharField(blank=True, max_length=500)
    owner = models.IntegerField('Skills Owner', blank=False, default=1)

    def __str__(self) -> str:
        return self.skills
    

# Just use the owner instead!

class ResumeUser(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('Email')
    contact = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.CASCADE)
    skillset = models.ForeignKey(Skills, blank=True, null=True, on_delete=models.CASCADE)
    experiences = models.ManyToManyField(Experience, blank=True, null=True)
    education = models.ManyToManyField(Education, blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
