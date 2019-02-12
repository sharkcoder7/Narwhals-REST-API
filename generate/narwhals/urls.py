from django.conf.urls import patterns, url, include
from rest_framework import routers

from views import WorkoutDetail, WorkoutList, UserView
from views import ConfigView

router = routers.DefaultRouter()
router.register(r'accounts', UserView, 'list')

urlpatterns = patterns(
    '',
    url(r'^narwhals/', include(router.urls)),
    url(r'^workouts/$', WorkoutList.as_view()),
    url(r'^workouts/(?P<pk>[0-9]+)/$', WorkoutDetail.as_view()),
    url(r'^config/$', ConfigView.as_view()),
)
