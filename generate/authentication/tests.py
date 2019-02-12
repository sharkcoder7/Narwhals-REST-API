import json

from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory

from django.conf import settings

from models import User, Swimmer
from authentication.models import SWIMMING
from views import UserList


class CreateUserTest(APITestCase):
    def setup(self):
        self.api_key = settings.API_KEY
        #self.superuser = User.objects.create_superuser('vishnu@vishnu.com', 'vishnupassword')
        self.client.login(username='test@gmail.com', password='123456')
        self.data = {'email': 'test@gmail.com',
                     'id': 1,
                     'date_of_birth': '1989-09-26',
                     'position': 1,
                     'meters': 1,
                     'minutes': 1,
                     'strokes': 1,
                     'metersAverage': 1,
                     'minutesAverage': 1,
                     'city_id': 1,
                     'name': 'Alexander',
                     'surname': 'The Great',
                     'trend': 'down',
                     'bio': None,
                     'password': '12346',
                     'sport': SWIMMING
                     }
        self.login = {'username': 'test@gmail.com',
                      'password': '12346',
                      'sport': SWIMMING}

    def _clean(self):
        User.objects.all().delete()

    def _has_token(self, data):
        if 'data' in data and 'token' in data['data']:
            return True
        return False

    def test_can_create_user(self):
        self._clean()
        self.setup()
        response = self.client.post('/api/v1/users/?api_key=%s' % self.api_key,
                                    self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_check_session(self):
        self._clean()
        self.setup()

        # Create user first
        response = self.client.post('/api/v1/users/?api_key=%s' % self.api_key,
                                    self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Login to get the token
        response = self.client.post('/api/v1/api-token-auth/?api_key=%s&sport=%s' % (self.api_key,
                                                                                    SWIMMING),
                                   self.login)
        token_auth_resp = json.loads(response.content)
        self.assertEqual(self._has_token(token_auth_resp), True)
        token = token_auth_resp['data']['token']
        response = self.client.get('/api/v1/check-session/?api_key=%s&sport=%s' % (self.api_key,
                                                                                   SWIMMING),
                                  HTTP_AUTHORIZATION='Token {}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_users(self):
        self._clean()
        self.setup()

        # Create user first
        response = self.client.post('/api/v1/users/?api_key=%s' % self.api_key,
                                    self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Login to get the token
        response = self.client.post('/api/v1/api-token-auth/?api_key=%s&sport=%s' % (self.api_key,
                                                                                    SWIMMING),
                                   self.login)
        token_auth_resp = json.loads(response.content)
        self.assertEqual(self._has_token(token_auth_resp), True)
        token = token_auth_resp['data']['token']
        response = self.client.get('/api/v1/users/?api_key=%s&sport=%s' % (self.api_key,
                                                                           SWIMMING),
                                   HTTP_AUTHORIZATION='Token {}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
