from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'generate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('formulario.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^v1/api/', include('narwhals.urls', namespace='v1')),
)
