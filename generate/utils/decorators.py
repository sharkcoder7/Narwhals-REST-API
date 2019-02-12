import logging
from django.conf import settings

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from helpers import error_response
from authentication.models import SPORTS

logging.basicConfig(filename='/home/apelegrina/logs/user/narwhals.log',level=logging.DEBUG,
        format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

def api_key_checker(f):
    def wrapper(*args, **kwargs):
        for param in args:
            if isinstance(param, Request):
                request = param

        key_provided = request.GET.get('api_key', '')
        logging.debug('api key %s' % key_provided)
        if key_provided != getattr(settings, 'API_KEY'):
            return Response(error_response('Api key needed.'),
                            status=status.HTTP_400_BAD_REQUEST)
        return f(*args, **kwargs)
    return wrapper

def sport_checker(f):
    def wrapper(*args, **kwargs):
        for param in args:
            if isinstance(param, Request):
                request = param

        sport = request.data.get('sport', '')
        if sport == '':
            sport = request.GET.get('sport', '')
        if sport != '':
            try:
                str_sport = SPORTS[int(sport)]
            except:
                return Response(error_response('Sport %s doesnt exist.' % sport),
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(error_response('Sport cannot be empty.'),
                            status=status.HTTP_400_BAD_REQUEST)

        return f(*args, **kwargs)
    return wrapper

