import xlsxwriter
from django.http import HttpResponse
from .models import WeatherReport


def export_weather_to_xlsx(place=None, start_date=None, end_date=None):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=weather_report.xlsx'

    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    headers = ['Место', 'Дата', 'Температура (°C)', 'Влажность (%)', 'Давление (мм рт. ст.)',
               'Скорость ветра (м/с)', 'Направление ветра']
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    reports = WeatherReport.objects.all()
    if place:
        reports = reports.filter(place__name=place)
    if start_date:
        reports = reports.filter(report_date__gte=start_date)
    if end_date:
        reports = reports.filter(report_date__lte=end_date)

    for row_num, report in enumerate(reports, start=1):
        worksheet.write(row_num, 0, report.place.name)
        worksheet.write(row_num, 1, report.report_date.strftime('%Y-%m-%d %H:%M'))
        worksheet.write(row_num, 2, report.temperature)
        worksheet.write(row_num, 3, report.humidity)
        worksheet.write(row_num, 4, report.pressure)
        worksheet.write(row_num, 5, report.wind_speed)
        worksheet.write(row_num, 6, report.wind_direction)

    workbook.close()
    return response
