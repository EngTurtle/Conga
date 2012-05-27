__author__ = 'Oliver'

from django.http import HttpResponse
from django.utils.encoding import smart_str

def serve_file(request, download_file, save_as, content_type, **kwargs):
    """Lets the web server serve the file using the X-Sendfile extension"""
    response = HttpResponse(content_type = content_type)
    response[ 'X-Accel-Redirect' ] = download_file.url
    if save_as:
        response[ 'Content-Disposition' ] = smart_str(u'attachment; filename=%s' % save_as)
    else:
        response[ 'Content-Disposition' ] = smart_str(u'inline; filename=%s' % download_file.name.rsplit('/')[ -1 ])
    if download_file.size is not None:
        response[ 'Content-Length' ] = download_file.size
    return response
