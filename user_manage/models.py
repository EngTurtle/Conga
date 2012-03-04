from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User)
    student_number = models.SmallIntegerField(verbose_name = 'student number', primary_key = True)