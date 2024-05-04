from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import *


class PlaceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Place
        fields = "__all__"