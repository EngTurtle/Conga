# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from Course_Manage.models import Course

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