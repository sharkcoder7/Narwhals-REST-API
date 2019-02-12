from django.conf.urls import patterns, url, include

from views import ObtainAuthToken, CheckSession
from views import UserList, UserDetail

urlpatterns = patterns(
    '',
    url(r'users/$', UserList.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'api-token-auth/', ObtainAuthToken.as_view()),
    url(r'check-session/', CheckSession.as_view()),
)
