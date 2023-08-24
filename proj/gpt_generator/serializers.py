from rest_framework import serializers

from .models import GeneratedImage, GeneratedResponse


class GeneratedResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedResponse
        fields = ["content"]


class GeneratedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedImage
        fields = ["image"]
