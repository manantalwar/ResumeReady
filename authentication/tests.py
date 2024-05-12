from .forms import RegisterUsersForm
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib import messages
from django.urls import reverse
from model_bakery import baker
from .views import user_login, user_logout, user_register

# Create your tests here.

# Forms

class RegisterUsersFormTest(TestCase):
    def test_form_fields(self):
        form = RegisterUsersForm()
        self.assertTrue('username' in form.fields)
        self.assertTrue('first_name' in form.fields)
        self.assertTrue('last_name' in form.fields)
        self.assertTrue('password1' in form.fields)
        self.assertTrue('password2' in form.fields)
        
    def test_form_field_widgets(self):
        form = RegisterUsersForm()
        self.assertEqual(form.fields['first_name'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['last_name'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['username'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['password1'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['password2'].widget.attrs['class'], 'form-control')
        
    def test_help_text(self):
        form = RegisterUsersForm()
        self.assertIsNone(form.fields['username'].help_text)
        self.assertIsNone(form.fields['password1'].help_text)
        self.assertIsNone(form.fields['password2'].help_text)
        
    def test_valid_data(self):
        form_data = {
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegisterUsersForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'testpassword1',
            'password2': 'testpassword2',
        }
        form = RegisterUsersForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['The two password fields didn’t match.'])
        
    def test_username_already_exists(self):
        User.objects.create_user(username='existinguser', password='password')
        form_data = {
            'username': 'existinguser',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegisterUsersForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ["A user with that username already exists."])

# Views 

class AuthenticationViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')


    def test_user_login_view_post_failure(self):
        data = {
            'username': 'nonexistentuser',
            'password': 'invalidpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertRedirects(response, reverse('login')) 

    def test_user_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login')) 

    def test_user_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_user_register_view_post_success(self):
        data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(reverse('register'), data)
        self.assertRedirects(response, reverse('login'))

    def test_user_register_view_post_password_mismatch(self):
        data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'testpassword1',
            'password2': 'testpassword2',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)  


    def test_user_register_view_invalid_form(self):
        data = {}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200) 


