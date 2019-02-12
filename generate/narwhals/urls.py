from django.conf.urls import patterns, url, include

from views import WorkoutDetail, WorkoutList
from views import ConfigView

urlpatterns = patterns(
    '',
    url(r'^workouts/$', WorkoutList.as_view()),
    url(r'^workouts/(?P<pk>[0-9]+)/$', WorkoutDetail.as_view()),
    url(r'^config/$', ConfigView.as_view()),
)
