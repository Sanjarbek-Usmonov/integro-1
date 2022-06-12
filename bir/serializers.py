from rest_framework import serializers
from .models import Section, Singer, CHOICES

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

class SingerSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=CHOICES)
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'gender']
        model = Singer

class MusicSerializer(serializers.ModelSerializer):
    singer = serializers.RelatedField(source='Singer', read_only=True)