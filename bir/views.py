from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework import permissions, views, response, status, viewsets
from .models import Users, Section, Singer, Music
from .serializers import Userserializer, SectionSerializer, SingerSerializer, MusicSerializer
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
        

# class MusicAPIView(views.APIView):
#     def get(self, request):
#         query = Music.objects.all()
#         serializer = MusicSerializer(query, many=True)
#         return response.Response(serializer.data)

#     def post(self, request):
#         serializer = MusicSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return response.Response(serializer.data)
#         else:
#             return response.Response({"detail": "Music turini nomini kirit:"})


class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()

#     def create(self, request, *args, **kwargs):
#         data = {
#             "singer": request.POST.get('singer'),
#             "music": request.POST.get('music'),
#             "text": request.POST.get('text'),
#             "section": request.POST.get('section'),
#             }
#         s = Singer.objects.filter(id=data["singer"])
#         data["singer"] = s
#         serializer = self.serializer_class(data=data)  
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)  
#         else:
#             return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
