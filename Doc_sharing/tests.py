from django.contrib.auth.models import User
from django.test import TestCase
from Course_Manage.models import Course
from models import *
from django.db.utils import IntegrityError

__author__ = 'Oliver'

class File_type_test(TestCase):
    def setUp(self):
        """
        Creating the test environment
        """
        self.MSE160 = Course.objects.create(year = 1, course_code = 'MSE160', course_name = 'Molecules and Materials')
        self.ESC101 = Course.objects.create(year = 1, course_code = 'ESC101', course_name = 'Praxis I')
        self.notes = Doc_type.objects.create(name = "notes", weighting = 50)
        self.tests = Doc_type.objects.create(name = "test", weighting = 10)

    def test_retrieve(self):
        self.assertEquals(self.notes, Doc_type.objects.get(name = "notes"))

    def test_weight(self):
        self.assertGreater(self.notes.weighting, self.tests.weighting)

    def test_weight_unique(self):
        try:
            self.notes2 = Doc_type.objects.create(name = "notes2", weighting = 50)
        except IntegrityError:
            pass
        else:
            standardMsg = "Two types should not have the same weighting"
            self.fail(self._formatMessage(None, standardMsg))


class Course_document_test(TestCase):
    def setUp(self):
        """
        Creating the test environment
        """
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.MSE160 = Course.objects.create(year = 1, course_code = 'MSE160', course_name = 'Molecules and Materials')
        self.ESC101 = Course.objects.create(year = 1, course_code = 'ESC101', course_name = 'Praxis I')
        self.notes = Doc_type.objects.create(name = "notes", weighting = 50)
        self.tests = Doc_type.objects.create(name = "test", weighting = 10)

        self.doc1 = Test_document.objects.create(name = 'doc1', owner = self.user, text = 'a1b2c3d4')
        self.doc2 = Test_document.objects.create(name = 'doc2', owner = self.user, text = 'kjads;lk')

        self.course_doc_1 = Course_document.objects.create(name = 'doc1', course = self.MSE160,
                                                           owner = self.user, year = 2012,
                                                           type = self.notes, doc = self.doc1)
        self.course_doc_1 = Course_document.objects.create(name = 'doc2', course = self.ESC101,
                                                           owner = self.user, year = 2012,
                                                           type = self.tests, doc = self.doc2)