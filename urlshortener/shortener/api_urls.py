from django.urls import path
from .api_views import ShortURLAPIView, ShortURLStatsAPIView

urlpatterns = [
    path("shorten/", ShortURLAPIView.as_view()),
    path("shorten/<str:short_code>/", ShortURLAPIView.as_view()),
    path("shorten/<str:short_code>/stats/", ShortURLStatsAPIView.as_view()),
]
