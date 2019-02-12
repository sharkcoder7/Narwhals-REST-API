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


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),


class EntrenamientoList(APIView):
    """
    List all entrenamientos, or create a new entrenamiento.
    """
    def get(self, request, format=None):
        entrenamientos = Entrenamiento.objects.all()
        serializer = EntrenamientoSerializer(entrenamientos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EntrenamientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateRetrieveAPIView(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            generics.GenericAPIView):
    """
    Concrete view for creating or retrieving a model instance.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EntrenamientoDetail(CreateRetrieveAPIView):
    """
    API endpoint for entrenamientos.
    """
    queryset = Entrenamiento.objects.all()
    serializer_class = EntrenamientoSerializer
