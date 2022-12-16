"""
ASGI config for video project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to the
# Django settings module for this project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video.settings')

# Get the ASGI application for the project
application = get_asgi_application()
