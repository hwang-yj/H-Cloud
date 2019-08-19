# userauth/serializers.py

from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.version
        field = ('version')
