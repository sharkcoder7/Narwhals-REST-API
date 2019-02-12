from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.conf import settings

from models import User, Swimmer, Runner


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
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

    id = serializers.IntegerField(source='type.id')
    last_login = serializers.DateTimeField(source='type.last_login')
    email = serializers.EmailField(source='type.email')
    date_of_birth = serializers.DateField(source='type.date_of_birth')
    city_id = serializers.IntegerField(source='type.city_id')
    name = serializers.CharField(source='type.name')
    surname = serializers.CharField(source='type.surname')
    bio = serializers.CharField(source='type.bio')
    avatar = serializers.CharField(source='type.avatar')
    token = serializers.SerializerMethodField(source='type.token')

    specific_fields = ['position', 'meters', 'minutes', 'strokes',
                       'trend', 'type']

    class Meta:
        model = Swimmer
        fields = ('position', 'meters', 'minutes', 'strokes',
                  'trend', 'type',
                  # Generic fields
                  'id', 'last_login', 'email', 'date_of_birth',
                  'city_id', 'name', 'surname',
                  'bio', 'avatar', 'token')
        read_only_fields = ('position', 'meters', 'minutes', 'trend', 
                            'id', 'last_login')

    def get_token(self, user):
        token = Token.objects.get(user=user.type.id)
        return token.key

    def create(self, validated_data):
        user = Swimmer.objects.create(**validated_data)
        user.save()
        return user


class RunnerSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(source='type.id', required=False, allow_null=True)
    last_login = serializers.DateTimeField(source='type.last_login', required = False, allow_null=True)
    email = serializers.EmailField(source='type.email', required=False, allow_null=True)
    date_of_birth = serializers.DateField(source='type.date_of_birth', required=False, allow_null=True)
    city_id = serializers.IntegerField(source='type.city_id', required=False, allow_null=True)
    name = serializers.CharField(source='type.name', required=False, allow_null=True)
    surname = serializers.CharField(source='type.surname', required=False, allow_null=True)
    bio = serializers.CharField(source='type.bio', required=False, allow_null=True)
    #avatar = serializers.ImageField(source='type.avatar', required=False, allow_null=True)
    token = serializers.SerializerMethodField(source='type.token', required=False, allow_null=True)

    avatar = serializers.SerializerMethodField()

    specific_fields = ['position', 'meters', 'minutes',
                       'trend', 'type']

    class Meta:
        model = Runner
        fields = ('position', 'meters', 'minutes', 
                  'trend', 'type',
                  # Generic fields
                  'id', 'last_login', 'email', 'date_of_birth',
                  'city_id', 'name', 'surname',
                  'bio', 'avatar', 'token')
        read_only_fields = ('position', 'meters', 'minutes', 'trend',
                            'id', 'last_login')

    def get_token(self, user):
        token = Token.objects.get(user=user.type.id)
        return token.key

    def get_avatar(self, user):
        try:
            return settings.SERVER_URL + user.type.avatar.url
        except:
            return ''

    def create(self, validated_data):
        user = Runner.objects.create(**validated_data)
        user.save()
        return user

