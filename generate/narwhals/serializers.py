from rest_framework import serializers

from models import Workout

class WorkoutSerializer(serializers.ModelSerializer):

    #user = UserSerializer()

    class Meta:
        model = Workout
        fields = ('id', 'user', 'sport', 'description', 'dateStart',
                  'dateFinish', 'duration', 'distance', 'strokes',
                  'speedAverage', 'strokeAverage', 'difficulty', 'mood')

