__author__ = 'Oliver'

import sys

def django_path_to_system(path = ''):
    if sys.platform == 'win32':
        return path.replace('/', '\\')
    else:
        return path


def system_path_to_django(path = ''):
    return path.replace('\\', '/')

#def path_from_media_root(path = ''):
