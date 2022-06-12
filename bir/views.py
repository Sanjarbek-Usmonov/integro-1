from functools import partial
from gc import get_objects
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework import permissions, views, response, status
from .models import Users, Section, Singer
from .serializers import Userserializer, SectionSerializer, SingerSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404

class UsersListAPIView(ListAPIView):
    # permission_classes = (permissions.AllowAny)
    serializer_class = Userserializer
    queryset = Users.objects.all()

class SectionAPIView(views.APIView):
    def get(self, request):
        query = Section.objects.all()
        serializer = SectionSerializer(query, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data)
        else:
            return response.Response({"detail": "Music turini nomini kirit:"})

    
class SectionDetailAPIView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Section, pk=pk)


    def put(self, request, pk):
        section = self.get_object(pk)
        serializer = SectionSerializer(instance=section, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        section = self.get_object(pk)
        section.delete()
        return response.Response({"detail": "deleted"})
        

class SingerAPIView(views.APIView):
    def get(self, request):
        query = Singer.objects.all()
        serializer = SingerSerializer(query, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data)
        else:
            return response.Response({"detail": "nimadir kirit"})

class SingerDetailAPIView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Singer, pk=pk)

    def put(self, request, pk):
        singer = self.get_object(pk)
        serializer = SingerSerializer(instance=singer, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
            singer = self.get_object(pk)
            serializer = SingerSerializer(instance=singer, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        singer = self.get_object(pk)
        singer.delete()
        return response.Response({"detail": "deleted"})
        

