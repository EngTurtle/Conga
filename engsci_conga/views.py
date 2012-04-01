__author__ = 'Oliver Liang, Brian To'

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import *
from engsci_conga.forms import *
from django.http import HttpResponseRedirect
from filetransfers.api import prepare_upload
from django.contrib.auth.decorators import login_required

@login_required#(login_url=reverse('django.contrib.auth.views.login'))
def file_upload(request):
    view_url = reverse(file_upload)

    if request.method == 'POST':
        form = File_upload(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            sf = Student_file(course = cd['course'],
                              owner = request.user,
                              note = cd['note'],
                              name = cd['name'],
                              file_type = cd['file_type'],
                              year = cd['year']
            )
            sf.save()
            return HttpResponseRedirect(reverse('engsci_conga.views.courses_view',
                                                #'engsci_conga.views.home'
                                                kwargs = {'course': str(cd['course'])}
            ))
    else:
        form = File_upload

    upload_url, upload_data = prepare_upload(request, view_url)

    return render_to_response('upload_form.html', {'form': form, 'upload_url': upload_url, 'upload_data': upload_data},
                              context_instance = RequestContext(request))


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
    is_logged_in = False
    if request.user.is_authenticated():
        is_logged_in = True
    courses = Course.objects.all()
    courses = [dict(course_name = c.course_name, course_code = c.course_code, course_year = c.year,
                    course_url = '/course/%s/' % c.course_code.lower()) for c in courses]
    return render_to_response('home.html', {'course_list': courses,
                                            'is_logged_in': is_logged_in}, context_instance = RequestContext(request))

    # TODO add a builtin login box


def courses_view(request, course):
    """
	This view gives a dictionary to the template in the following format:
	{'course_name' : course name in a unicode string,
	 'course_code' : course code in a unicode string,
	 'types' : [ {type_name=..., type_weight=...int}, repeating...]
	 'files': [ {name=..., type=...str, type_weighting=...int, url=..., year=...int}, repeating ] }
	"""
    is_logged_in = False
    if request.user.is_authenticated():
        is_logged_in = True
    c = get_object_or_404(Course, course_code = course.upper())
    files = Student_file.objects.filter(course = c)
    types = File_type.objects.all()

    files_by_type = []
    for t in types:
        files_by_type.append(dict(name = t.type_name, files = files.filter(file_type = t)))

    response = {'course': c,
                'types': types,
                'files': files_by_type,
                'is_logged_in': is_logged_in}
    return render_to_response('course.html', response, context_instance = RequestContext(request))


def list_all_courses(request):
    """
    This view returns a list of all courses.
    """
    courses = Course.objects.all()
    courses = [dict(course_name = c.course_name, course_code = c.course_code, course_year = c.year,
                    course_url = '/course/%s/' % c.course_code.lower()) for c in courses]

    response = {'courses': courses}

    return render_to_response('all_courses.json', response, context_instance = RequestContext(request))
