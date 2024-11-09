from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News, Place, WeatherReport


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(News, NewsAdmin)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinates', 'rating')
    search_fields = ('name',)


@admin.register(WeatherReport)
class WeatherReportAdmin(admin.ModelAdmin):
    list_display = ('place', 'temperature', 'humidity', 'pressure', 'wind_speed', 'report_date')
    list_filter = ('place', 'report_date')
