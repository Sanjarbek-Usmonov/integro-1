from django.urls import path
from .views import UsersListAPIView, SectionAPIView, SectionDetailAPIView, SingerAPIView, SingerDetailAPIView

urlpatterns = [
    path('', UsersListAPIView.as_view()),
    path('sections', SectionAPIView.as_view()),
    path('section/<int:pk>', SectionDetailAPIView.as_view()),
    path('singers', SingerAPIView.as_view()),
    path('singer/<int:pk>', SingerDetailAPIView.as_view()),
]