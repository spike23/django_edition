from rest_framework import serializers
from .models import Room
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # Сериализация пользователя

    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializers(serializers.ModelSerializer):
    # Сериализация комнат чата

    creator = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ('creator', 'invited', 'date')
