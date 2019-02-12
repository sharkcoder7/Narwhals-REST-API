from rest_framework import parsers, renderers
from rest_framework import viewsets, exceptions
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Django REST Authentication
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission

from utils.helpers import success_response, error_response
from serializers import SwimmerSerializer, RunnerSerializer
from serializers import UserSerializer
from authentication.models import User, SPORTS
from authentication.models import Swimmer, Runner
from utils.decorators import api_key_checker
from utils.decorators import sport_checker


SAFE_METHODS = ['POST']


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated()):
            return True
        return False


class UserList(APIView):
    """
    Creates a new user.
    """
    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @api_key_checker
    @sport_checker
    def get(self, request, format=None):
        sport = int(request.data.get('sport', ''))
        if sport == 0:
            swimmers = Swimmer.objects.all()
            serializer = SwimmerSerializer(swimmers, many=True)
        elif sport == 1:
            runners = Runner.objects.all()
            serializer = RunnerSerializer(runners, many=True)
        return Response(success_response(serializer.data))

    @api_key_checker
    @sport_checker
    def post(self, request, format=None, sport=None):
        try:
            email = request.data['email']
            existing_user = User.objects.get(email=email)
            return Response(error_response('User with email %s already exists.'
                                           % email),
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        sport = int(request.data.get('sport', '0'))
        user = UserSerializer()
        user_fields = [key for key in user.get_fields().keys()]
        user_data = { key: request.data[key]
                      for key in user_fields
                      if key in request.data }
        user_data['type_id'] = SPORTS[sport][1] 
        user_serializer = UserSerializer(data=user_data)

        # Create base user
        if user_serializer.is_valid():
            if not 'password' in request.data:
                return Response(error_response('Password not provided.'),
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                user = user_serializer.save()
                user.set_password(request.data['password'])
                user.save()

        # Create specific user (swimmer, runner...)
        if sport == 0:
            swimmer = SwimmerSerializer()
            swimmer_fields = [key for key in SwimmerSerializer.specific_fields]
            swimmer_data = { key: request.data[key]
                            for key in swimmer_fields
                            if key in request.data }
            swimmer_data['type'] = user.id
            serializer = SwimmerSerializer(data=swimmer_data)

        elif sport == 1:
            runner = RunnerSerializer()
            runner_fields = [key for key in RunnerSerializer.specific_fields]
            runner_data = { key: request.data[key]
                            for key in runner_fields
                            if key in request.data }
            runner_data['type'] = user.id
            serializer = RunnerSerializer(data=runner_data)

        if serializer.is_valid():
            sport_user = serializer.save()
            return Response(success_response(serializer.data),
                            status=status.HTTP_201_CREATED)

        return Response(error_response(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @api_key_checker
    @sport_checker
    def put(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        user_serializer = UserSerializer()
        sport = int(request.data.get('sport', ''))
        user_data = { key: request.data[key]
                      for key in user_serializer.fields
                      if key in request.data }
        for (key, value) in user_data.items():
            setattr(user, key, value)
        user.save()
        if sport == 0:
            try:
                swimmer = Swimmer.objects.get(type__id=user.id)
            except Swimmer.DoesNotExist:
                return Response(error_response('Swimmer does not exist'),
                                status=status.HTTP_404_NOT_FOUND)
            swimmer_fields = [key for key in SwimmerSerializer.specific_fields]
            swimmer_data = { key: request.data[key]
                            for key in swimmer_fields
                            if key in request.data }
            swimmer_data['type'] = user.id
            serializer = SwimmerSerializer(swimmer, data=swimmer_data, partial=True)

        elif sport == 1:
            try:
                runner = Runner.objects.get(type__id=user.id)
            except Runner.DoesNotExist:
                return Response(error_response('Runner does not exist'),
                                status=status.HTTP_404_NOT_FOUND)
            runner_fields = [key for key in RunnerSerializer.specific_fields]
            runner_data = { key: request.data[key]
                            for key in runner_fields
                            if key in request.data }
            runner_data['type'] = user.id
            serializer = RunnerSerializer(runner, data=runner_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(success_response(serializer.data),
                            status=status.HTTP_201_CREATED)
        return Response(error_response(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)

    """
    @api_key_checker
    def delete(self, request, format=None):
        user = self.get_object(pk, request.user)
        user.delete()
        return Response(success_response("null"),
                        status=status.HTTP_204_NO_CONTENT)
    """

class ObtainAuthToken(APIView):
    """
    Overriding this Django REST class
    to also return the User.
    """
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    @api_key_checker
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        sport = int(request.data.get('sport', ''))
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            if sport == 0:
                swimmer = Swimmer.objects.get(type=user.id)
                user_serialized = SwimmerSerializer(user)
            elif sport == 1:
                runner = Runner.objects.get(type=user.id)
                user_serialized = RunnerSerializer(runner)
            return Response(success_response(user_serialized.data))
        else:
            return Response(error_response("User or password incorrect."))


class CheckSession(APIView):
    """
    Validates if the session is still valid.
    """
    permission_classes = (IsAuthenticated,)

    @api_key_checker
    @sport_checker
    def get(self, request, *args, **kwargs):
        try:
            provided_token = request.META['HTTP_AUTHORIZATION']
            provided_token = provided_token.replace('Token ', '')
            token = Token.objects.select_related('user').get(key=provided_token)
        except Exception as e:
            # modify the original exception response
            raise exceptions.APIException("Token not valid.")

        if not token.user.is_active:
            # can also modify this exception message
            return Response(error_response("User inactive or deleted."))

        try:
            sport = int(request.data.get('sport', ''))
        except:
            sport = int(request.GET.get('sport', ''))

        if sport == 0:
            swimmer = Swimmer.objects.get(type=request.user.id)
            user_serialized = SwimmerSerializer(swimmer)
        elif sport == 1:
            runner = Runner.objects.get(type=request.user.id)
            user_serialized = RunnerSerializer(runner)

        return Response(success_response(user_serialized.data))

