__author__ = 'Oliver'

from django.test import TestCase
from Course_Manage.models import Course
from models import Doc_type
from django.db.utils import IntegrityError

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
