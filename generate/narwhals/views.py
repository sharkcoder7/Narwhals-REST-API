import logging

from django.shortcuts import render
from django.http import Http404

from models import Entrenamiento
from serializers import EntrenamientoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from permissions import IsStaffOrTargetUser
from serializers import UserSerializer

# Django REST Authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

logging.basicConfig(filename='/home/apelegrina/logs/user/narwhals.log',level=logging.DEBUG,
        format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")


class UserView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = UserSerializer
    model = User

    """
    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),
    """

class EntrenamientoList(APIView):
    """
    List all entrenamientos, or create a new entrenamiento.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        entrenamientos = Entrenamiento.objects.filter(user=request.user)
        serializer = EntrenamientoSerializer(entrenamientos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EntrenamientoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EntrenamientoDetail(APIView):
    """
    API endpoint for entrenamientos.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk, user):
        logging.debug("request. Id %s and user %s" % (pk, user))
        try:
            return Entrenamiento.objects.get(id=pk, user=user)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        entrenamiento = self.get_object(pk, request.user)
        serializer = EntrenamientoSerializer(entrenamiento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        entrenamiento = self.get_object(pk, request.user)
        serializer = EntrenamientoSerializer(entrenamiento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        entrenamiento = self.get_object(pk, request.user)
        entrenamiento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
