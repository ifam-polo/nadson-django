"""
WSGI config for projeto projeto.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoprojeto.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

load_dotenv()
application = get_wsgi_application()
