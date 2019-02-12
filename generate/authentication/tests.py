#from django.core.urlresolvers import reverse
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory

from django.conf import settings

from models import User
from views import UserList


class CreateUserTest(APITestCase):
    def setup(self):
        self.api_key = settings.API_KEY
        self.superuser = User.objects.create_superuser('vishnu@vishnu.com', '1989-09-26', 'vishnupassword')
        self.client.login(username='vishnu', password='vishnupassword')
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
                     'password': '12346'
                     }
        self.token = Token.objects.get(user_id=self.superuser.id)

    def test_can_create_user(self):
        self.setup()
        response = self.client.post('/api/v1/users/?api_key=%s' % self.api_key,
                                    self.data, 
                                    HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_check_session(self):
        self.setup()
        response = self.client.get('/api/v1/check-session/?api_key=%s' % self.api_key,
                                  HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_users(self):
        self.setup()
        response = self.client.get('/api/v1/users/?api_key=%s' % self.api_key,
                                   HTTP_AUTHORIZATION='Token {}'.format(self.token))
        print response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
