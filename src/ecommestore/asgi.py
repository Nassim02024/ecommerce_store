"""
ASGI config for ecommestore project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.ecommestore.settings')

application = get_asgi_application()
