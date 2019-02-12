import logging

from django.shortcuts import render
from django.http import Http404

from models import Workout
from serializers import WorkoutSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

# Django REST Authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from serializers import UserSerializer
from utils import success_response, error_response


logging.basicConfig(filename='/home/apelegrina/logs/user/narwhals.log',level=logging.DEBUG,
        format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")


class UserView(viewsets.ModelViewSet):
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutDetail(APIView):
    """
    API endpoint for workout.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk, user):
        logging.debug("request. Id %s and user %s" % (pk, user))
        try:
            return Workout.objects.get(id=pk, user=user)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        workout = self.get_object(pk, request.user)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        workout = self.get_object(pk, request.user)
        serializer = WorkoutSerializer(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workout = self.get_object(pk, request.user)
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConfigView(APIView):
    """
    API endpoint for config initialization.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        config = {'min_app_version': 1,
                  'force_update': 'true',}
        return Response(config, status=status.HTTP_200_OK)
