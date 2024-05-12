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
        return self.first_name + ' ' + self.last_name
    
    def __repr__(self) -> str:
        return {
            'first_name': self.first_name, 
            'last_name': self.last_name, 
            'phone': self.phone, 
            'linkedin':self.linkedin,
            'website':self.website,
            'address':self.address,
        }

class Experience(models.Model):
    role = models.CharField('Role', max_length=30)
    company = models.CharField('Company', max_length=30)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    description = models.TextField(blank=True)
    owner = models.IntegerField('Experience Owner', blank=False, default=1)

    def __str__(self) -> str:
        return self.role
    
    def __repr__(self) -> str:
        return {
            'role': self.role, 
            'company': self.company, 
            'start_date': self.start_date, 
            'end_date':self.end_date,
            'description':self.description,
        }

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
    
    def __repr__(self) -> str:
        return {
            'degree': self.degree, 
            'major': self.major, 
            'institution': self.institution, 
            'start_date': self.start_date, 
            'end_date':self.end_date,
            'coursework':self.coursework,
            'gpa':self.gpa,
        }

class Skills(models.Model):
    skills = models.CharField(blank=True, max_length=500)
    owner = models.IntegerField('Skills Owner', blank=False, default=1)

    def __str__(self) -> str:
        return self.skills
    
    def __repr__(self) -> str:
        return {
            'skills': self.skills, 
        }

class Jobs(models.Model):
    description = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    owner = models.IntegerField('Job Owner', blank=False, default=1)

    def __str__(self) -> str:
        return self.description
    
    def __repr__(self) -> str:
        return {
            'description': self.description, 
            'qualifications':self.qualifications,
        }

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
