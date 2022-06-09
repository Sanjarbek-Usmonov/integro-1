from django.urls import path
from .views import UsersListAPIView, SectionAPIView, SectionDetailAPIView

urlpatterns = [
    path('', UsersListAPIView.as_view()),
    path('sections', SectionAPIView.as_view()),
    path('section/<int:pk>', SectionDetailAPIView.as_view()),
]