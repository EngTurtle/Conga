__author__ = 'Oliver'

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from models import *

#def file_upload(request):

def home(request):
    course_list = {}
    for y in range(1,5):
        course_year = Course.objects.filter(year=y)
        course_year = [dict(course_name=c.course_name,
                            course_code=c.course_code,
                            course_url='/course/%s/' % c.course_code.lower()) for c in course_year]
        course_list[y] = course_year
    return render_to_response('base.html', {'course_list': course_list})


def coursesview(request, course):
    """
	This view gives a dictionary to the template in the following format:
	{'course_name' : course name in a unicode string,
	'course_code' : course code in a unicode string,
	'files_by_type': {'type name 1' : [('filename1', file_url1)
									   ('filename2', file_url2)...],
					  'type name 2' : [('filename1', file_url1)
									   ('filename2', file_url2)...],
					   ...}
	"""
    c = get_object_or_404(Course, course_code=course.upper())
    types = File_type.objects.all()
    files_by_type = {}
    for this_type in types:
        files_of_type = Student_file.objects.filter(file_type=this_type,
        											course=c)
        files_by_type[this_type.type_name] = [(f.name, f.note.url) for f in
                                                          files_of_type]

    response = {'course_name' : c.course_name,
    			'course_code' : c.course_code,
    			'files_by_type': files_by_type}
    return HttpResponse(str(response))
    # TODO need a template here