# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from Course_Manage.models import Course
from Doc_sharing.models import Course_document, Doc_type

def course_list(request):
    courses = Course.objects.all()
    return render_to_response('home.html', {'course_list': courses},
                              context_instance = RequestContext(request))

    # TODO add a builtin login box


def list_all_courses(request):
    """
    This view returns a list of all courses.
    """
    courses = Course.objects.all()
    courses = [ dict(course_name = c.course_name, course_code = c.course_code, course_year = c.year,
                     course_url = '/course/%s/' % c.course_code.lower()) for c in courses ]

    response = {'courses': courses}

    return render_to_response('all_courses.json', response, mimetype = 'application/json',
                              context_instance = RequestContext(request))


def courses_view(request, course):
    """
	This view gives a dictionary to the template in the following format:
	{'course_name' : course name in a unicode string,
	 'course_code' : course code in a unicode string,
	 'types' : [ {type_name=..., type_weight=...int}, repeating...]
	 'files': [ {name=..., type=...str, weighting=...int, url=..., year=...int}, repeating ] }
	"""
    c = get_object_or_404(Course, course_code = course.upper())
    files = Course_document.objects.filter(course = c)
    types = Doc_type.objects.all()

    files_by_type = [ ]
    for t in types:
        files_by_type.append(dict(name = t.type_name, files = files.filter(file_type = t)))

    response = {'course': c,
                'types': types,
                'files': files_by_type}
    return render_to_response('course.html', response, context_instance = RequestContext(request))