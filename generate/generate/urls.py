from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api/v1/', include('narwhals.urls', namespace='v1')),
    url(r'^api/v1/', include('authentication.urls', namespace='v1')),
    url(r'^api/v1/accounts/', include('authemail.urls', namespace='v1')),
)
