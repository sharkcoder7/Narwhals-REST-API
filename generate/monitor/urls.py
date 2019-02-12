from django.conf.urls import patterns, url, include

from views import MonitorView

urlpatterns = patterns(
    '',
    url(r'^check/$', MonitorView.as_view())
)
