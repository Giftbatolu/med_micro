from rest_framework import serializers
from .models import Microoganism

class MicroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microoganism
        fields = '__all__'