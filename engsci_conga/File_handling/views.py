from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from filetransfers.api import serve_file
from engsci_conga.models import Student_file
from django.http import Http404, HttpResponseRedirect

__author__ = 'Oliver'

def download_handler(request, user, pk):
    upload = get_object_or_404(Student_file, pk = pk)
    if upload.owner.username != user:
        raise Http404
    return serve_file(request, upload.note, save_as = True)


@login_required
def delete_handler(request, pk):
    f = get_object_or_404(Student_file, pk = pk)
    if f.owner.username != request.user:
        raise Http404
    f.delete()
    return HttpResponseRedirect(reverse('engsci_conga.views.courses_view',
                                        kwargs = {'course': str(f.course)}
    )
    )

    # TODO write a signal handler to delete the actual file when the student_file is deleted