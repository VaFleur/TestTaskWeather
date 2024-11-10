from rest_framework import viewsets
from .models import News, WeatherReport
from .serializers import NewsSerializer
from django.shortcuts import render
from django.http import HttpResponse
from .utils import export_weather_to_xlsx


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


def export_weather_view(request):
    place_name = request.GET.get('place')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    queryset = WeatherReport.objects.all()

    if place_name:
        queryset = queryset.filter(place__name=place_name)
    if start_date:
        queryset = queryset.filter(report_date__gte=start_date)
    if end_date:
        queryset = queryset.filter(report_date__lte=end_date)

    if not queryset.exists():
        return HttpResponse("Нет данных для экспорта", content_type='text/plain')

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=filtered_weather_reports.xlsx'

    return export_weather_to_xlsx(queryset=queryset, response=response)
