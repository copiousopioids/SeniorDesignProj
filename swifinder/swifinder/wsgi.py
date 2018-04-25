"""
WSGI config for swifinder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swifinder.settings")

application = get_wsgi_application()


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
