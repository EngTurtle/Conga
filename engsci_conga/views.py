__author__ = 'Oliver Liang, Brian To'

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import *
from engsci_conga.forms import *
from django.http import HttpResponseRedirect
from filetransfers.api import prepare_upload
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@login_required
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
                                                kwargs = {'course': str(cd['course'])}
            ))
    else:
        form = File_upload

    upload_url, upload_data = prepare_upload(request, view_url)

    return render_to_response('upload_form.html', {'form': form, 'upload_url': upload_url, 'upload_data': upload_data},
                              context_instance = RequestContext(request))


def courses_view(request, course):
    """
	This view gives a dictionary to the template in the following format:
	{'course_name' : course name in a unicode string,
	 'course_code' : course code in a unicode string,
	 'types' : [ {type_name=..., type_weight=...int}, repeating...]
	 'files': [ {name=..., type=...str, type_weighting=...int, url=..., year=...int}, repeating ] }
	"""
    c = get_object_or_404(Course, course_code = course.upper())
    files = Student_file.objects.filter(course = c)
    types = File_type.objects.all()

    files_by_type = []
    for t in types:
        files_by_type.append(dict(name = t.type_name, files = files.filter(file_type = t)))

    response = {'course': c,
                'types': types,
                'files': files_by_type}
    return render_to_response('course.html', response, context_instance = RequestContext(request))

