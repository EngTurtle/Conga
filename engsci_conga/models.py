__author__ = 'Oliver'

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	year = models.SmallIntegerField(verbose_name='Course Year')
	course_code = models.CharField(verbose_name='Course Code', max_length=7, primary_key=True)
	course_name = models.CharField(verbose_name='Course Name',max_length=50)

	def __unicode__(self):
		return self.course_code

class Student(models.Model):

	user = models.ForeignKey(User)
	student_number = models.SmallIntegerField(verbose_name='student number', primary_key=True)

class Student_file(models.Model):
	course = models.ForeignKey(Course)
	note = models.FileField(upload_to='notes')
	owner = models.ForeignKey(Student)
	last_modified = models.DateTimeField(auto_now=True)

	TYPE_CHOICES = ((u'NO', u'Notes'),
	                (u'FE', u'Final Exam'),
	                (u'TQ', u'Tests & Quizzes'),
	                (u'AS', u'Assignments'))
	note_type = models.CharField(max_length=2, choices=TYPE_CHOICES)

	def __unicode__(self):
		return self.note.name
