from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News, Place, WeatherReport
from .utils import export_weather_to_xlsx


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
    actions = ['export_selected']

    def export_selected(self, request, queryset):
        place = request.GET.get('place')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        response = export_weather_to_xlsx(place, start_date, end_date)
        return response

    export_selected.short_description = "Экспортировать в xlsx"

