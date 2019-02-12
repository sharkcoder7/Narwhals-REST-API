from django.conf import settings

from rest_framework import serializers

from models import SwimWorkout, RunWorkout


class SwimWorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = SwimWorkout
        fields = ('id', 'user', 'description', 'dateStart',
                  'dateFinish', 'duration', 'distance', 'strokes',
                  'speedAverage', 'strokeAverage', 'difficulty',
                  'mood', 'file_log')

    def to_representation(self, workout):
        """
        Override the representation to display the full file url path
        """
        representation = super(SwimWorkoutSerializer, self).to_representation(workout)
        full_path = ''
        if bool(workout.file_log):
            full_path = settings.SERVER_URL + workout.file_log.url
        representation['file_log'] = full_path
        return representation


class RunWorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = RunWorkout
        fields = ('id', 'user', 'description', 'dateStart',
                  'dateFinish', 'duration', 'distance',
                  'speed', 'difficulty', 'maxSpeed', 'ascendedMeters',
                  'descendedMeters', 'maxAltitude', 'minAltitude',
                  'mood', 'file_log')

    def to_representation(self, workout):
        """
        Override the representation to display the full file url path
        """
        representation = super(RunWorkoutSerializer, self).to_representation(workout)
        full_path = ''
        if bool(workout.file_log):
            full_path = settings.SERVER_URL + workout.file_log.url
        representation['file_log'] = full_path
        return representation
