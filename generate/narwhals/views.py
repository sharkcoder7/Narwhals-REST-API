import logging

from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

# Django REST Authentication
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from models import Workout
from authentication.models import User
from serializers import WorkoutSerializer
from utils.helpers import success_response, error_response
from utils.decorators import api_key_checker

logging.basicConfig(filename='/home/apelegrina/logs/user/narwhals.log',level=logging.DEBUG,
        format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")


class WorkoutList(APIView):
    """
    List all workouts, or create a new workout.
    """

    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        workouts = Workout.objects.filter(user=request.user)
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(success_response(serializer.data))

    def post(self, request, format=None):
        data = request.data
        data["user"] = request.user.id
        serializer = WorkoutSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(success_response(serializer.data),
                            status=status.HTTP_201_CREATED)
        return Response(error_response(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)


class WorkoutDetail(APIView):
    """
    API endpoint for workout.
    """

    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            workout = Workout.objects.get(id=pk, user=request.user)
        except:
            return Response(error_response("Workout with id %s not found" % pk),
                            status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutSerializer(workout)
        return Response(success_response(serializer.data), status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        workout = self.get_object(pk, request.user)
        serializer = WorkoutSerializer(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_response(serializer.data),
                            status=status.HTTP_201_CREATED)
        return Response(error_response(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workout = self.get_object(pk, request.user)
        workout.delete()
        return Response(success_response("null"),
                        status=status.HTTP_204_NO_CONTENT)


class ConfigView(APIView):
    """
    API endpoint for config initialization.
    """

    permission_classes = (AllowAny,)

    @api_key_checker
    def get(self, request):
        key_provided = request.GET.get('api_key', '')
        version = getattr(settings, 'min_app_version', 1)
        force_update = getattr(settings, 'force_update', True)
        config = {'min_app_version': version,
                  'force_update': force_update,}
        return Response(success_response(config), status=status.HTTP_200_OK)
