# Rest imports
from rest_framework import serializers

# Models
from heroes.models import Hero

# Serializer
class HeroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hero
        fields = '__all__'