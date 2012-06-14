__author__ = 'Oliver Liang, Brian To'

from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from Doc_sharing.forms import *
from django.http import HttpResponseRedirect
from filetransfers.api import prepare_upload
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from Doc_sharing.File_handling.views import download_handler, delete_handler

@csrf_protect
@login_required
def file_upload(request):
    view_url = reverse(file_upload)

    if request.method == 'POST':
        form = File_upload(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            sf = Course_document(course = cd[ 'course' ],
                                 owner = request.user,
                                 note = cd[ 'note' ],
                                 name = cd[ 'name' ],
                                 file_type = cd[ 'type' ],
                                 year = cd[ 'year' ]
            )
            sf.save()
            return HttpResponseRedirect(reverse('Doc_sharing.views.courses_view',
                                                kwargs = {'course': str(cd[ 'course' ])}
            ))
    else:
        form = File_upload

    upload_url, upload_data = prepare_upload(request, view_url)

    return render_to_response('upload_form.html', {'form': form, 'upload_url': upload_url, 'upload_data': upload_data},
                              context_instance = RequestContext(request))

# TODO create a page to view doc info before downloading
def doc_page(request, user, pk):
    return download_handler(request, user, pk)


def doc_delete(request, user, pk):
    return delete_handler(request, user, pk)