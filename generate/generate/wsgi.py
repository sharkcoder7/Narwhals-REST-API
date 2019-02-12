"""
WSGI config for generate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

"""
import os
import site
import sys

site.addsitedir('/home/apelegrina/webapps/generate_webapp/lib/python2.7/site-packages/')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/apelegrina/webapps/generate_webapp')
sys.path.append('/home/apelegrina/webapps/generate_webapp/generate')

os.environ['DJANGO_SETTINGS_MODULE'] = 'generate.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/apelegrina/webapps/generate_webapp/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))
"""

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'generate.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
