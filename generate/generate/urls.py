from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.authtoken import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^v1/api/', include('narwhals.urls', namespace='v1')),
    url(r'^api-token-auth/', views.obtain_auth_token),
)
