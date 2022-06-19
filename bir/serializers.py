from asyncore import read
from dataclasses import fields
from imp import source_from_cache
from pyexpat import model
from rest_framework import serializers
from .models import Music, Section, Singer, CHOICES

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
    singer = serializers.PrimaryKeyRelatedField(queryset=Singer.objects.all()) 
    music = serializers.FileField()
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())

    class Meta:
        fields = ['id', 'singer', 'text', 'music', 'section']
        model = Music

    # def create(self, validated_data):
    #     # print(validated_data)
    #     singer = validated_data.pop()
    #     # print(singer)
    #     # singer_instance = Singer.objects.get(id=singer)
    #     # print(singer_instance)
    #     music_instance = Music.objects.create(**validated_data)
    #     return music_instance