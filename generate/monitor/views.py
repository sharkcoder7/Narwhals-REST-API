from django.shortcuts import render

from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from utils.helpers import success_response


class MonitorView(APIView):
    """
    API endpoint to update the landing.
    """

    permission_classes = (AllowAny,)

    def get(self, request):
        data = {'landing-doswim': { 'status': 'online',
                                    'url': 'www.landing-doswim.com' },
                'landing-dorun': {'status': 'offline',
                                    'url': 'www.landing-dorun.com' },
                'landing-narwhale': { 'status': 'offline',
                                      'url': 'www.landing-narwhale.com' }}
        return Response(success_response(data), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        user_id = request.user.id
        sport = int(request.data.get('sport', ''))

        if sport == SWIMMING:
            sport_user = Swimmer.objects.get(type__id=user_id)
            data['user'] = sport_user.id
            serializer = SwimWorkoutSerializer(data=data)
        elif sport == RUNNING:
            sport_user = Runner.objects.get(type__id=user_id)
            data['user'] = sport_user.id
            serializer = RunWorkoutSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(success_response(serializer.data),
                            status=status.HTTP_201_CREATED)
        return Response(error_response(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)

