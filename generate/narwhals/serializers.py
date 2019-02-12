from rest_framework import serializers

from models import SwimWorkout, RunWorkout


class SwimWorkoutSerializer(serializers.ModelSerializer):

    file = serializers.SerializerMethodField()

    class Meta:
        model = SwimWorkout
        fields = ('id', 'user', 'description', 'dateStart',
                  'dateFinish', 'duration', 'distance', 'strokes',
                  'speedAverage', 'strokeAverage', 'difficulty',
                  'mood', 'file')

    def get_file(self, workout):
        try:
            return settings.SERVER_URL + workout.file_log.url
        except:
            return ''


class RunWorkoutSerializer(serializers.ModelSerializer):

    file = serializers.SerializerMethodField()

    class Meta:
        model = RunWorkout
        fields = ('id', 'user', 'description', 'dateStart',
                  'dateFinish', 'duration', 'distance',
                  'speed', 'difficulty', 'maxSpeed', 'ascendedMeters',
                  'descendedMeters', 'maxAltitude', 'minAltitude',
                  'mood', 'file')

    def get_file(self, workout):
        try:
            return settings.SERVER_URL + workout.file_log.url
        except:
            return ''

