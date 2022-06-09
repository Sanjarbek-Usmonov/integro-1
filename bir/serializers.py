from rest_framework import serializers
from .models import Section

class Userserializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()
    

class SectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        fields = ['id', 'name']
        model = Section
