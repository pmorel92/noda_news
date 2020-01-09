"""
WSGI config for nodanews_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
#from dj_static import Cling


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nodanews_project.settings')

#application = Cling(get_wsgi_application())
application = get_wsgi_application()
application = WhiteNoise(application, root='/nodanews_project/static')
