__author__ = 'Oliver'

from django.shortcuts import render_to_response, get_object_or_404
from models import *

# TODO def file_upload(request):

def home(request):
    """
    The dictionary this function gives to the template is the the following format:
    {'course_list': {[ {course_name='Praxis II', course_code='ESC102', course_url='/courses/esc102/', course_year=1},
                       {course_name='Calculus II', course_code='MAT195', course_url='/course/mat105/', course_year=1},
                       {course_name='Engineering Design', course_code'AER201', course_url='/courses/aer201/',
                       course_year=2} ]
                    }
    }
    """
    courses = Course.objects.all()
    courses = [dict(course_name = c.course_name, course_code = c.course_code, course_year = c.year,
                    course_url = '/course/%s/' % c.course_code.lower()) for c in courses]
    return render_to_response('home.html', {'course_list': courses})


def coursesview(request, course):
    """
	This view gives a dictionary to the template in the following format:
	{'course_name' : course name in a unicode string,
	 'course_code' : course code in a unicode string,
	 'types' : [ {type_name=..., type_weight=...int}, repeating...]
	 'files': [ {name=..., type=...str, type_weighting=...int, url=..., year=...int}, repeating ] }
	"""
    c = get_object_or_404(Course, course_code = course.upper())
    del course
    files = Student_file.objects.filter(course = c)
    types = File_type.objects.all()
    response = {'course_name': c.course_name,
                'course_code': c.course_code,
                'types': types,
                'files': files}
    return render_to_response('course.html', {'response': response})