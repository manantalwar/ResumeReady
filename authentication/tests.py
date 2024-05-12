from .forms import RegisterUsersForm
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib import messages
from django.urls import reverse
from model_bakery import baker

# Create your tests here.

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
        # Create a user with the username 'existinguser'
        User.objects.create_user(username='existinguser', password='password')
        
        # Try to register a new user with the same username
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

