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

from models import SwimWorkout, RunWorkout
from authentication.models import Swimmer, Runner
from serializers import SwimWorkoutSerializer, RunWorkoutSerializer
from paginator import CustomPagination

from utils.helpers import success_response, error_response
from utils.decorators import api_key_checker
from utils.decorators import sport_checker


logging.basicConfig(filename='/home/apelegrina/logs/user/narwhals.log',level=logging.DEBUG,
        format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")


class WorkoutList(APIView):
    """
    List all workouts, or create a new workout.
    """

    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @sport_checker
    @api_key_checker
    def get(self, request, format=None):
        paginator = CustomPagination()
        sport = int(request.data.get('sport', ''))
        if sport == 0:
            try:
                swimmer = Swimmer.objects.get(type__id=request.user.id)
                swim_workouts = SwimWorkout.objects.filter(user=swimmer).order_by('-dateStart')
                serializer = SwimWorkoutSerializer(swim_workouts, many=True)
            except:
                return Response(error_response('This user has not a swimmer profile enabled.'),
                                status=status.HTTP_404_NOT_FOUND)

        elif sport == 1:
            try:
                runner = Runner.objects.get(type_id=request.user.id)
                run_workouts = RunWorkouts.objects.filter(user=request.user).order_by('-dateStart')
                serializer = RunWorkoutSerializer(run_workouts, many=True)
            except:
                return Response(error_response('This user has not a runner profile enabled.'),
                                status=status.HTTP_404_NOT_FOUND)

        return paginator.get_paginated_response(success_response(serializer.data))

    @sport_checker
    @api_key_checker
    def post(self, request, format=None):
        data = request.data
        user_id = request.user.id
        sport = int(request.data.get('sport', ''))

        if sport == 0:
            sport_user = Swimmer.objects.get(type__id=user_id)
            data['user'] = sport_user.id
            serializer = SwimWorkoutSerializer(data=data)
        elif sport == 1:
            sport_user = Runner.objects.get(type__id=user_id)
            data['user'] = sport_user.id
            serializer = RunWorkoutSerializer(data=data)

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

    @sport_checker
    @api_key_checker
    def get(self, request, pk, format=None):
        sport = int(request.data.get('sport', ''))

        if sport == 0:
            try:
                workout = SwimWorkout.objects.get(id=pk)
                serializer = SwimWorkoutSerializer(workout)
            except:
                return Response(error_response("Workout with id %s not found" % pk),
                                status=status.HTTP_404_NOT_FOUND)
        elif sport == 1:
            try:
                workout = RunWorkout.objects.get(id=pk)
                serializer = RunWorkoutSerializer(workout)
            except:
                return Response(error_response("Workout with id %s not found" % pk),
                                status=status.HTTP_404_NOT_FOUND)

        return Response(success_response(serializer.data), status=status.HTTP_200_OK)

    @sport_checker
    @api_key_checker
    def put(self, request, pk, format=None):
        sport = int(request.data.get('sport', ''))

        if sport == 0:
            try:
                workout = SwimWorkout.objects.get(id=pk)
                serializer = SwimWorkoutSerializer(workout,
                                                   data=request.data,
                                                   partial=True)
            except:
                return Response(error_response("Workout with id %s not found" % pk),
                                status=status.HTTP_404_NOT_FOUND)
        elif sport == 1:
            try:
                workout = RunWorkout.objects.get(id=pk)
                serializer = RunWorkoutSerializer(workout,
                                                  data=request.data,
                                                  partial=True)
            except:
                return Response(error_response("Workout with id %s not found" % pk),
                                status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save()
            return Response(success_response(serializer.data),
                            status=status.HTTP_201_CREATED)
        return Response(error_response(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)

    @sport_checker
    @api_key_checker
    def delete(self, request, pk, format=None):
        sport = int(request.data.get('sport', ''))

        if sport == 0:
            try:
                workout = SwimWorkout.objects.get(id=pk)
            except:
                return Response(error_response("Workout with id %s not found" % pk),
                                status=status.HTTP_404_NOT_FOUND)
        elif sport == 1:
            try:
                workout = RunWorkout.objects.get(id=pk)
            except:
                return Response(error_response("Workout with id %s not found" % pk),
                                status=status.HTTP_404_NOT_FOUND)

        workout.delete()
        return Response(success_response("null"),
                        status=status.HTTP_200_OK)


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
