from rest_framework import serializers
from .models import DomesticNews, OverseasNews

class DomesticNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomesticNews
        fields = '__all__'

class OverseasNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverseasNews
        fields = '__all__'