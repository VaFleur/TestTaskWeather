from django.contrib import admin
from django.http import HttpResponse
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
    actions = ['export_filtered']

    def export_filtered(self, request, queryset):
        if queryset.exists():
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = 'attachment; filename=filtered_weather_reports.xlsx'

            return export_weather_to_xlsx(queryset=queryset, response=response)
        else:
            self.message_user(request, "Нет данных для экспорта", level='warning')

    export_filtered.short_description = "Экспортировать в xlsx"
