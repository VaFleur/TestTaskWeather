from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, export_weather_view

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('export-weather/', export_weather_view, name='export_weather'),
]
