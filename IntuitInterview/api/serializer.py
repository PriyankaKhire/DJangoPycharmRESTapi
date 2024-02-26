from rest_framework import serializers

from api.models import Player


class IntuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'