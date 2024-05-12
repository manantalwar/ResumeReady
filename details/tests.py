from model_bakery import baker
from .models import Education, Contact, Experience, Skills, Jobs
from django.core.exceptions import ValidationError
from django.db.models import URLField, DateField
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm
from django.contrib.auth.models import User

# Create your tests here.

# Testing Models 

class ContactModelTests(TestCase):

    def setUp(self):
        self.contacts = baker.make('Contact', _quantity=100)
    
    def test_contact_creation(self):
        self.assertTrue(len(self.contacts) == 100)
        for elem in self.contacts:
            self.assertTrue(isinstance(elem, Contact))
    
    def test_first_name_label(self):
        for elem in self.contacts:
            field_label = elem._meta.get_field('first_name').verbose_name
            self.assertEqual(field_label, 'First Name')
    
    def test_first_name_max_length(self):
        for elem in self.contacts:
            max_length = elem._meta.get_field('first_name').max_length
            self.assertEqual(max_length, 100)

    def test_last_name_label(self):
        for elem in self.contacts:
            field_label = elem._meta.get_field('last_name').verbose_name
            self.assertEqual(field_label, 'Last Name')
    
    def test_last_name_max_length(self):
        for elem in self.contacts:
            max_length = elem._meta.get_field('last_name').max_length
            self.assertEqual(max_length, 100)
    
    def test_phone_label(self):
        for elem in self.contacts:
            field_label = elem._meta.get_field('phone').verbose_name
            self.assertEqual(field_label, 'Phone')
    
    def test_phone_max_length(self):
        for elem in self.contacts:
            max_length = elem._meta.get_field('phone').max_length
            self.assertEqual(max_length, 10)
    
    def test_linkedin_label(self):
        for elem in self.contacts:
            field_label = elem._meta.get_field('linkedin').verbose_name
            self.assertEqual(field_label, 'LinkedIn')
    
    def test_webiste_label(self):
        for elem in self.contacts:
            field_label = elem._meta.get_field('website').verbose_name
            self.assertEqual(field_label, 'Website')
    
    def test_address_label(self):
        for elem in self.contacts:
            field_label = elem._meta.get_field('address').verbose_name
            self.assertEqual(field_label, 'Address')

    def test_address_max_length(self):
        for elem in self.contacts:
            max_length = elem._meta.get_field('address').max_length
            self.assertEqual(max_length, 200)
    
    def test_str(self):
        for elem in self.contacts:        
            expected_object_name = f'{elem.first_name} {elem.last_name}'
        self.assertEqual(str(elem), expected_object_name)

    def test_owner_is_integer(self):
        for elem in self.contacts:
            self.assertTrue(isinstance(elem.owner, int))
    
    def test_linkedin_is_URL(self):
        for elem in self.contacts:
            self.assertTrue(isinstance(elem._meta.get_field('linkedin'), URLField))
    
    def test_website_is_URL(self):
        for elem in self.contacts:
            self.assertTrue(isinstance(elem._meta.get_field('website'), URLField))


class ContactInstanceTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            phone='1234567890',
            linkedin='https://www.linkedin.com/in/johndoe',
            website='https://www.example.com',
            address='123 Main St',
            owner=1
        )
        self.invalid = Contact.objects.create(
            first_name='Invalid',
            last_name='User',
            phone='abcdefgh',
            linkedin='fake',
            website='trash',
            address='123 Main St',
            owner=2
        )

    def test_contact_creation(self):
        self.assertTrue(isinstance(self.contact, Contact))
        self.assertEqual(self.contact.first_name, 'John')
        self.assertEqual(self.contact.last_name, 'Doe')
        self.assertEqual(self.contact.phone, '1234567890')
        self.assertEqual(self.contact.linkedin, 'https://www.linkedin.com/in/johndoe')
        self.assertEqual(self.contact.website, 'https://www.example.com')
        self.assertEqual(self.contact.address, '123 Main St')
        self.assertEqual(self.contact.owner, 1)

    def test_string_representation(self):
        self.assertEqual(str(self.contact), 'John Doe')

    def test_repr_method(self):
        expected_repr = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'linkedin': 'https://www.linkedin.com/in/johndoe',
            'website': 'https://www.example.com',
            'address': '123 Main St',
        }
        self.assertEqual(self.contact.__repr__(), expected_repr)

    def test_blank_fields(self):
        contact = Contact.objects.create(first_name='Jane', last_name='Doe', phone='', linkedin='', website='', address='', owner=1)
        self.assertTrue(isinstance(contact, Contact))
        self.assertEqual(contact.phone, '')
        self.assertEqual(contact.linkedin, '')
        self.assertEqual(contact.website, '')
        self.assertEqual(contact.address, '')

    def test_valid_instance(self):
        self.assertFalse(self.contact.clean_fields())

    def test_invalid_instance(self):
        with self.assertRaises(ValidationError):
            self.invalid.clean_fields()

    def test_owner_is_integer(self):
        self.assertTrue(isinstance(self.contact.owner, int))


class ExperienceModelTests(TestCase):

    def setUp(self):
        self.experiences = baker.make('Experience', _quantity=100)
    
    def test_contact_creation(self):
        self.assertTrue(len(self.experiences) == 100)
        for elem in self.experiences:
            self.assertTrue(isinstance(elem, Experience))
    
    def test_role_label(self):
        for elem in self.experiences:
            field_label = elem._meta.get_field('role').verbose_name
            self.assertEqual(field_label, 'Role')
    
    def test_role_max_length(self):
        for elem in self.experiences:
            max_length = elem._meta.get_field('role').max_length
            self.assertEqual(max_length, 30)

    def test_comapny_label(self):
        for elem in self.experiences:
            field_label = elem._meta.get_field('company').verbose_name
            self.assertEqual(field_label, 'Company')
    
    def test_company_max_length(self):
        for elem in self.experiences:
            max_length = elem._meta.get_field('company').max_length
            self.assertEqual(max_length, 30)
    
    def test_start_date_label(self):
        for elem in self.experiences:
            field_label = elem._meta.get_field('start_date').verbose_name
            self.assertEqual(field_label, 'Start Date')
    
    def test_end_date_label(self):
        for elem in self.experiences:
            field_label = elem._meta.get_field('end_date').verbose_name
            self.assertEqual(field_label, 'End Date')
    
    def test_str(self):
        for elem in self.experiences:        
            expected_object_name = f'{elem.role}'
        self.assertEqual(str(elem), expected_object_name)

    def test_owner_is_integer(self):
        for elem in self.experiences:
            self.assertTrue(isinstance(elem.owner, int))
    
    def test_start_date_is_date(self):
        for elem in self.experiences:
            self.assertTrue(isinstance(elem._meta.get_field('start_date'), DateField))
    
    def test_end_date_is_date(self):
        for elem in self.experiences:
            self.assertTrue(isinstance(elem._meta.get_field('end_date'), DateField))


class ExperienceInstanceTest(TestCase):
    def setUp(self):
        self.exp = Experience.objects.create(
            role="Software Engineer",
            company="Example Company",
            start_date=timezone.now(),
            end_date=timezone.now(),
            description="Worked on various projects",
            owner=1
        )

    def test_experience_creation(self):
        self.assertEqual(self.exp.role, "Software Engineer")
        self.assertEqual(self.exp.company, "Example Company")
        self.assertEqual(self.exp.description, "Worked on various projects")
        self.assertEqual(self.exp.owner, 1)

    def test_experience_str_representation(self):
        self.assertEqual(str(self.exp), "Software Engineer")

    def test_experience_repr_representation(self):
        exp_dict = self.exp.__repr__()
        self.assertEqual(exp_dict['role'], "Software Engineer")
        self.assertEqual(exp_dict['company'], "Example Company")

    def test_experience_update(self):
        new_role = "Senior Software Engineer"
        self.exp.role = new_role
        self.exp.save()
        updated_exp = Experience.objects.get(pk=self.exp.pk)
        self.assertEqual(updated_exp.role, new_role)

    def test_experience_query(self):
        queried_exp = Experience.objects.filter(role="Software Engineer").first()
        self.assertIsNotNone(queried_exp)
        self.assertEqual(queried_exp.company, "Example Company")

    def test_experience_end_date_greater_than_start_date(self):
        self.assertTrue(self.exp.end_date > self.exp.start_date)

    def test_experience_description_blank(self):
        exp = Experience.objects.create(
            role="Tester",
            company="Another Company",
            start_date=timezone.now(),
            end_date=timezone.now(),
            owner=2
        )
        self.assertEqual(exp.description, "")

    def test_experience_owner_default_value(self):
        exp = Experience.objects.create(
            role="Designer",
            company="Design Studio",
            start_date=timezone.now(),
            end_date=timezone.now(),
        )
        self.assertEqual(exp.owner, 1)

class EducationModelTests(TestCase):

    def setUp(self):
        self.experiences = baker.make('Education', _quantity=100)
    
    def test_education_creation(self):
        self.assertTrue(len(self.experiences) == 100)
        for elem in self.experiences:
            self.assertTrue(isinstance(elem, Education))
    
    def test_degree_label(self):
        for elem in self.experiences:
            field_label = elem._meta.get_field('degree').verbose_name
            self.assertEqual(field_label, 'Degree')
    
    def test_degree_max_length(self):
        for elem in self.experiences:
            max_length = elem._meta.get_field('degree').max_length
            self.assertEqual(max_length, 30)

    def test_major_label(self):
        for elem in self.experiences:
            field_label = elem._meta.get_field('major').verbose_name
            self.assertEqual(field_label, 'Major')
    
    def test_major_max_length(self):
        for elem in self.experiences:
            max_length = elem._meta.get_field('major').max_length
            self.assertEqual(max_length, 30)
    
    def test_institution_label(self):
        for elem in self.experiences:
            field_label = elem._meta.get_field('institution').verbose_name
            self.assertEqual(field_label, 'Institution')
    
    def test_institution_max_length(self):
        for elem in self.experiences:
            max_length = elem._meta.get_field('institution').max_length
            self.assertEqual(max_length, 30)
    
    def test_start_date_label(self):
        for elem in self.experiences:
            field_label = elem._meta.get_field('start_date').verbose_name
            self.assertEqual(field_label, 'Start Date')
    
    def test_end_date_label(self):
        for elem in self.experiences:
            field_label = elem._meta.get_field('end_date').verbose_name
            self.assertEqual(field_label, 'End Date')
    
    def test_str(self):
        for elem in self.experiences:        
            expected_object_name = f'{elem.degree}'
        self.assertEqual(str(elem), expected_object_name)

    def test_owner_is_integer(self):
        for elem in self.experiences:
            self.assertTrue(isinstance(elem.owner, int))
    
    def test_start_date_is_date(self):
        for elem in self.experiences:
            self.assertTrue(isinstance(elem._meta.get_field('start_date'), DateField))
    
    def test_end_date_is_date(self):
        for elem in self.experiences:
            self.assertTrue(isinstance(elem._meta.get_field('end_date'), DateField))


class EducationInstanceTests(TestCase):
    def setUp(self):
        self.edu = Education.objects.create(
            degree="Bachelor of Science",
            major="Computer Science",
            institution="University of Example",
            start_date=timezone.now(),
            end_date=timezone.now(),
            coursework="Completed various courses",
            gpa=3.5,
            owner=1
        )

    def test_education_creation(self):
        self.assertEqual(self.edu.degree, "Bachelor of Science")
        self.assertEqual(self.edu.major, "Computer Science")
        self.assertEqual(self.edu.institution, "University of Example")
        self.assertEqual(self.edu.coursework, "Completed various courses")
        self.assertEqual(self.edu.gpa, 3.5)
        self.assertEqual(self.edu.owner, 1)

    def test_education_str_representation(self):

        self.assertEqual(str(self.edu), "Bachelor of Science")

    def test_education_repr_representation(self):
        edu_dict = self.edu.__repr__()
        self.assertEqual(edu_dict['degree'], "Bachelor of Science")
        self.assertEqual(edu_dict['major'], "Computer Science")

    def test_education_end_date_greater_than_start_date(self):
        self.assertTrue(self.edu.end_date > self.edu.start_date)

    def test_education_coursework_blank(self):
        edu = Education.objects.create(
            degree="Master of Science",
            major="Data Science",
            institution="Another University",
            start_date=timezone.now(),
            end_date=timezone.now(),
            gpa=4.0,
            owner=2
        )
        self.assertEqual(edu.coursework, "")

    def test_education_owner_default_value(self):
        edu = Education.objects.create(
            degree="Associate Degree",
            major="Arts",
            institution="Community College",
            start_date=timezone.now(),
            end_date=timezone.now(),
            gpa=3.2,
        )
        self.assertEqual(edu.owner, 1)

class SkillsModelTests(TestCase):

    def setUp(self):
        self.skills = baker.make('Skills', _quantity=100)
    
    def test_skills_creation(self):
        self.assertTrue(len(self.skills) == 100)
        for elem in self.skills:
            self.assertTrue(isinstance(elem, Skills))
    
    def test_skills_label(self):
        for elem in self.skills:
            field_label = elem._meta.get_field('skills').verbose_name
            self.assertEqual(field_label, 'skills')
    
    def test_skills_max_length(self):
        for elem in self.skills:
            max_length = elem._meta.get_field('skills').max_length
            self.assertEqual(max_length, 500)
    
    def test_str(self):
        for elem in self.skills:        
            expected_object_name = f'{elem.skills}'
        self.assertEqual(str(elem), expected_object_name)

    def test_owner_is_integer(self):
        for elem in self.skills:
            self.assertTrue(isinstance(elem.owner, int))


class SkillsInstanceTests(TestCase):
    def setUp(self):
        self.skills = Skills.objects.create(
            skills="Python, Django, HTML, CSS",
            owner=1
        )

    def test_skills_creation(self):
        self.assertEqual(self.skills.skills, "Python, Django, HTML, CSS")
        self.assertEqual(self.skills.owner, 1)

    def test_skills_str_representation(self):
        self.assertEqual(str(self.skills), "Python, Django, HTML, CSS")

    def test_skills_repr_representation(self):
        skills_dict = self.skills.__repr__()
        self.assertEqual(skills_dict['skills'], "Python, Django, HTML, CSS")

    def test_skills_blank_field(self):
        skills = Skills.objects.create(owner=2)
        self.assertEqual(skills.skills, "")

    def test_skills_owner_default_value(self):
        skills = Skills.objects.create(skills="Java, JavaScript", owner=1)
        self.assertEqual(skills.owner, 1)

class JobsModelTests(TestCase):

    def setUp(self):
        self.jobs = baker.make('Jobs', _quantity=100)
    
    def test_skills_creation(self):
        self.assertTrue(len(self.jobs) == 100)
        for elem in self.jobs:
            self.assertTrue(isinstance(elem, Jobs))
    
    def test_description_label(self):
        for elem in self.jobs:
            field_label = elem._meta.get_field('description').verbose_name
            self.assertEqual(field_label, 'Description')
    
    def test_qualification_label(self):
        for elem in self.jobs:
            field_label = elem._meta.get_field('qualifications').verbose_name
            self.assertEqual(field_label, 'qualifications')
    
    def test_description_label(self):
        for elem in self.jobs:
            field_label = elem._meta.get_field('specifications').verbose_name
            self.assertEqual(field_label, 'specifications')

    def test_str(self):
        for elem in self.jobs:        
            expected_object_name = f'{elem.description}'
        self.assertEqual(str(elem), expected_object_name)

    def test_owner_is_integer(self):
        for elem in self.jobs:
            self.assertTrue(isinstance(elem.owner, int))

class JobsInstanceTests(TestCase):
    def setUp(self):
        self.job = Jobs.objects.create(
            description="Software Developer",
            qualifications="Bachelor's degree in Computer Science",
            specifications="Experience with Python, Django",
            owner=1
        )

    def test_job_creation(self):
        self.assertEqual(self.job.description, "Software Developer")
        self.assertEqual(self.job.qualifications, "Bachelor's degree in Computer Science")
        self.assertEqual(self.job.specifications, "Experience with Python, Django")
        self.assertEqual(self.job.owner, 1)

    def test_job_str_representation(self):
        self.assertEqual(str(self.job), "Software Developer")

    def test_job_repr_representation(self):
        job_dict = self.job.__repr__()
        self.assertEqual(job_dict['description'], "Software Developer")
        self.assertEqual(job_dict['qualifications'], "Bachelor's degree in Computer Science")

    def test_job_blank_fields(self):
        job = Jobs.objects.create(owner=2)
        self.assertEqual(job.description, "")
        self.assertEqual(job.qualifications, "")
        self.assertEqual(job.specifications, "")

    def test_job_owner_default_value(self):
        job = Jobs.objects.create(description="Data Scientist", qualifications="Master's degree in Statistics", owner=1)
        self.assertEqual(job.owner, 1)

# Views 

class AddContactViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='test_user', password='test_password')
        self.user2 = User.objects.create_user(username='test_user_2', password='test_password_2')
        self.user1.save()
        self.user2.save()    

    def test_get_request(self):
        response = self.client.get(reverse('add-contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'details/add_contact.html')
        self.assertFalse(response.context['submitted'])

    
    def test_post_request_valid_form(self):
        self.client.login(username='test_user', password='test_password')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'linkedin': 'https://www.linkedin.com/in/johndoe',
            'website': 'https://www.example.com',
            'address': '123 Main St',
        }
        response = self.client.post('add-contact', data)
        print(response.content)
        self.assertEqual(response.status_code, 302) 
        #self.assertTrue(Contact.objects.filter(first_name='John').exists())

    def test_get_request_submitted(self):
        response = self.client.get(reverse('add-contact') + '?submitted=True')
        self.assertTrue(response.context['submitted'])


class UpdateContactViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='test_user', password='test_password')
        self.user2 = User.objects.create_user(username='test_user_2', password='test_password_2')
        self.user1.save()
        self.user2.save()
        # self.client.login(username='test_user', password='test_password')
        self.contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            phone='1234567890',
            linkedin='https://www.linkedin.com/in/johndoe',
            website='https://www.example.com',
            address='123 Main St',
            owner=1
        )
        self.contact.save()
    
    
    def test_post_request_valid_form(self):
        self.client.login(username='test_user', password='test_password')
        data = {
            'first_name': 'Test',
            'last_name': 'Doe',
            'phone': '1234567890',
            'linkedin': 'https://www.linkedin.com/in/johndoe',
            'website': 'https://www.example.com',
            'address': '123 Main St',
            'owner':1,
        }
        response = self.client.post(reverse('update-contact'), data, kwargs={'pk': self.contact.pk})
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Contact.objects.filter(first_name='Test').exists())