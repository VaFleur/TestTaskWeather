import pandas as pd
from django.core.management.base import BaseCommand
from news.models import Place
from django.contrib.gis.geos import Point


class Command(BaseCommand):
    help = 'Импорт Примечательных мест из xlsx-файла'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Путь к xlsx-файлу')

    def handle(self, *args, **options):
        file_path = options['file_path']
        data = pd.read_excel(file_path)

        for index, row in data.iterrows():
            name = row['Название места']
            latitude = row['Широта']
            longitude = row['Долгота']
            rating = row['Рейтинг']

            point = Point(longitude, latitude)

            Place.objects.create(
                name=name,
                coordinates=point,
                rating=rating
            )

        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))
