from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from django.shortcuts import render
from django.http import HttpResponse
from .utils import export_weather_to_xlsx


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


def export_weather_view(request):
    place = request.GET.get('place')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    response = export_weather_to_xlsx(place, start_date, end_date)
    return response
