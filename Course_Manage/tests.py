"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from models import *

class course_model_test(TestCase):
    def setUp(self):
        """
        Creating the test environment
        """
        self.MSE160 = Course.objects.create(year = 1, course_code = 'MSE160', course_name = 'Molecules and Materials')
        self.ESC101 = Course.objects.create(year = 1, course_code = 'ESC101', course_name = 'Praxis I')
        self.AER201 = Course.objects.create(year = 2, course_code = 'aer201', course_name = 'Engineering Design')
        self.ECE256 = Course.objects.create(year = 2, course_code = 'ECE256',
                                            course_name = 'Digital and Computer Systems')
        self.ECE352 = Course.objects.create(year = 3, course_code = 'ECE352', course_name = 'Computer Organization')
        self.ESC401 = Course.objects.create(year = 4, course_code = 'ESC401', course_name = 'Capstone')

    def test_Course_code(self):
        self.assertEqual(self.MSE160.course_code, 'MSE160')
        # auto set the course code to uppercase
        self.assertEqual(self.AER201.course_code, 'AER201')

    def test_FilterByYear(self):
        first_year = Course.objects.filter(year = 1)
        self.assertIn(self.ESC101, first_year)
        self.assertNotIn(self.ECE352, first_year)

    def test_course_name(self):
        self.assertEqual(self.ESC401.course_name, 'Capstone')

    def test_url(self):
        self.assertIn(self.ECE352.course_code.lower(), self.ECE352.get_absolute_url())


class course_view_test(TestCase):
    def setUp(self):
        self.MSE160 = Course.objects.create(year = 1, course_code = 'MSE160', course_name = 'Molecules and Materials')
        self.ESC101 = Course.objects.create(year = 1, course_code = 'ESC101', course_name = 'Praxis I')
        self.AER201 = Course.objects.create(year = 2, course_code = 'aer201', course_name = 'Engineering Design')
        self.ECE256 = Course.objects.create(year = 2, course_code = 'ECE256',
                                            course_name = 'Digital and Computer Systems')
        self.ECE352 = Course.objects.create(year = 3, course_code = 'ECE352', course_name = 'Computer Organization')
        self.ESC401 = Course.objects.create(year = 4, course_code = 'ESC401', course_name = 'Capstone')

    def test_CourseView(self):
        c = Client()
        self.assertTemplateUsed(c.get('/'), 'home.html')
