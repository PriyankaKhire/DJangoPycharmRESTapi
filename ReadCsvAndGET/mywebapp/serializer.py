from rest_framework import serializers

from mywebapp.models import Alphabets


class AlphabetSerializer(serializers.ModelSerializer):
    class Meta:
        # Import the Data model to serialize
        model = Alphabets
        fields = '__all__'

class AlphabetNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alphabets
        fields = ['name']