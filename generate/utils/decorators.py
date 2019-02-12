import logging
from django.conf import settings

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from helpers import error_response

logging.basicConfig(filename='/home/apelegrina/logs/user/narwhals.log',level=logging.DEBUG,
        format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

def api_key_checker(f):
    def wrapper(*args, **kwargs):
        for param in args:
            if isinstance(param, Request):
                request = param

        key_provided = request.GET.get('api_key', '')
        logging.debug("api key %s" % key_provided)
        if key_provided != getattr(settings, 'API_KEY'):
            return Response(error_response("Api key needed."),
                            status=status.HTTP_400_BAD_REQUEST)
        return f(*args, **kwargs)
    return wrapper

