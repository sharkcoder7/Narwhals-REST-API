from django.conf.urls import patterns, url, include

from views import ObtainAuthToken, CheckSession
from views import UserList

urlpatterns = patterns(
    '',
    url(r'users/$', UserList.as_view()),
    url(r'api-token-auth/', ObtainAuthToken.as_view()),
    url(r'check-session/', CheckSession.as_view()),
)
