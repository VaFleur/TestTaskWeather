import xlsxwriter


def export_weather_to_xlsx(queryset, response):
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    # Заголовки
    headers = ['Место', 'Дата', 'Температура (°C)', 'Влажность (%)', 'Давление (мм рт. ст.)', 'Скорость ветра (м/с)', 'Направление ветра']
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    for row_num, report in enumerate(queryset, start=1):
        worksheet.write(row_num, 0, report.place.name)
        worksheet.write(row_num, 1, report.report_date.strftime('%Y-%m-%d %H:%M'))
        worksheet.write(row_num, 2, report.temperature)
        worksheet.write(row_num, 3, report.humidity)
        worksheet.write(row_num, 4, report.pressure)
        worksheet.write(row_num, 5, report.wind_speed)
        worksheet.write(row_num, 6, report.wind_direction)

    workbook.close()
    return response
