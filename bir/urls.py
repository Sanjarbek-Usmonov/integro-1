from django.urls import path
from .views import UsersListAPIView, SectionAPIView, SectionDetailAPIView, SingerAPIView, SingerDetailAPIView, MusicViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', UsersListAPIView.as_view()),
    path('sections', SectionAPIView.as_view()),
    path('section/<int:pk>', SectionDetailAPIView.as_view()),
    path('singers', SingerAPIView.as_view()),
    path('singer/<int:pk>', SingerDetailAPIView.as_view()),
    # path('music', MusicAPIView.as_view()),
]
router = DefaultRouter()  
router.register('music', MusicViewSet, basename='music')
urlpatterns += router.urls