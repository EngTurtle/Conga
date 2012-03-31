from django.shortcuts import get_object_or_404
from filetransfers.api import serve_file
from engsci_conga.models import Student_file
from django.http import Http404

__author__ = 'Oliver'

def download_handler(request, user, pk):
    upload = get_object_or_404(Student_file, pk = pk)
    if upload.owner.username != user:
        raise Http404
    return serve_file(request, upload.note, save_as = True)