from rest_framework import serializers
from rest_framework.authtoken.models import Token

from models import User

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'last_login', 'email', 'date_of_birth', 'position',
                  'meters', 'minutes', 'strokes', 'metersAverage',
                  'minutesAverage', 'city_id', 'name', 'surname', 'trend',
                  'bio', 'avatar', 'token', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('is_admin', 'is_active',)

    def get_token(self, user):
        token = Token.objects.get(user=user.id)
        return token.key

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
