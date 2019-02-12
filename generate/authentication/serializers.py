from rest_framework import serializers
from rest_framework.authtoken.models import Token

from models import Swimmer, Runner

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = Swimmer
        fields = ('id', 'last_login', 'email', 'date_of_birth', 
                  'city_id', 'name', 'surname',
                  'bio', 'avatar', 'token')
        write_only_fields = ('password',)
        read_only_fields = ('is_admin', 'is_active',)

    def get_token(self, user):
        token = Token.objects.get(user=user.id)
        return token.key

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user


class SwimmerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Swimmer
        fields = ('position', 'meters', 'minutes', 'strokes',
                  'trend', 'bio')

    def create(self, validated_data):
        user = Swimmer.objects.create(**validated_data)
        user.save()
        return user


class RunnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Runner
        fields = ('position', 'meters', 'minutes', 
                  'trend', 'bio')

    def create(self, validated_data):
        user = Runner.objects.create(**validated_data)
        user.save()
        return user

