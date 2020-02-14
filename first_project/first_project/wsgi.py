"""
WSGI config for first_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import dotenv #api data
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

#for api
dotenv.load_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
)

#This code snippet has an additional os.path.dirname() because
#wsgi.py needs to look two directories back to find the .env file.
#This snippet is not the same as the one used for manage.py.

application = get_wsgi_application()
