from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api/v1/', include('narwhals.urls', namespace='v1')),
    url(r'^api/v1/', include('authentication.urls', namespace='v1')),
    url(r'^api/v1/accounts/', include('authemail.urls', namespace='v1')),

    # Reset password
    url(r'^user/password/reset/$', 
        auth_views.password_reset, 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^user/password/reset/done/$',
        auth_views.password_reset_done),
    (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        auth_views.password_reset_confirm, 
        {'post_reset_redirect' : '/user/password/done/'}),
    (r'^user/password/done/$', 
        auth_views.password_reset_complete),
)
