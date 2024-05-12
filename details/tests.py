from django.test import TestCase
from model_bakery import baker
from pprint import pprint
from .models import Education

# Create your tests here.
class TestEducationModel(TestCase):
    def setUp(self):
        self.education = baker.make('Education')
        pprint(self.customer.__dict__)
