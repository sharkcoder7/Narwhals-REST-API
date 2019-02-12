import logging

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

# Django REST Authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from models import Workout
from serializers import WorkoutSerializer
from serializers import UserSerializer
from utils import success_response, error_response


logging.basicConfig(filename='/home/apelegrina/logs/user/narwhals.log',level=logging.DEBUG,
        format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")


class UserView(viewsets.ModelViewSet):
    """
    API endpoint for User
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = UserSerializer
    model = User


class WorkoutList(APIView):
    """
    List all workouts, or create a new workout.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        workouts = Workout.objects.filter(user=request.user)
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(success_response(serializer.data))

    def post(self, request, format=None):
        serializer = WorkoutSerializer(data=request.data, many=True)
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

    authentication_classes = (TokenAuthentication,)
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

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        version = settings.get('min_app_version', 1)
        force_update = settings.get('force_update', 'true')
        config = {'min_app_version': version,
                  'force_update': force_update,}
        return Response(config, status=status.HTTP_200_OK)
