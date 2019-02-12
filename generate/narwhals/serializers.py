from rest_framework import serializers

from models import Entrenamiento, SPORT_CHOICES, FILE_TYPE_CHOICES

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


"""
class EntrenamientoSerializer(serializers.Serializer):

     user = UserSerializer()
     id = serializers.IntegerField()
     sport = serializers.ChoiceField(choices=SPORT_CHOICES)
     description = serializers.CharField(max_length=500)
     dateStart = serializers.DateTimeField()
     dateEnd = serializers.DateTimeField()
     duration = serializers.IntegerField()
     distance = serializers.FloatField()
     speedMax = serializers.FloatField()
     speedAvg = serializers.FloatField()
     heightMax = serializers.IntegerField()
     heightMin = serializers.IntegerField()
     metersUploaded = serializers.IntegerField()
     metersDownloaded = serializers.IntegerField()
     filetype = serializers.ChoiceField(choices=FILE_TYPE_CHOICES)
     filepath = serializers.CharField() 
     isPrivate = serializers.BooleanField()
     isSynchronized = serializers.BooleanField()
     difficulty = serializers.IntegerField()
"""

class EntrenamientoSerializer(serializers.ModelSerializer):

    #user = serializers.RelatedField(source='user', read_only=True)

    class Meta:
        model = Entrenamiento
