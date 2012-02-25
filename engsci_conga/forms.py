__author__ = 'Oliver'
from django import forms
from models import Course

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course

class File_upload(forms.Form):
	ALL_COURSES = Course.objects.all()
	COURSE_CHOICES = [(c.course_code, c.course_name) for c in ALL_COURSES]
	ALL_TYPE = Course.objects.all()
	TYPE_CHOICES = [(c.course_code, c.course_name) for c in ALL_TYPE]

	course = forms.ChoiceField(choices=COURSE_CHOICES)
	type = forms.ChoiceField(choices=TYPE_CHOICES)
	file = forms.FileField(required=True)

	# TODO write a function that renames the uploaded files in a structured
	# way to prevent blackboard's one filename problem