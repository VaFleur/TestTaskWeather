from django.db import models
from django.contrib.gis.db import models as gis_models
from PIL import Image
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='news_images/')
    preview_image = models.ImageField(upload_to='news_images/previews/', blank=True, null=True)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.main_image and not self.preview_image:
            img = Image.open(self.main_image.path)
            img.thumbnail((200, 200))
            preview_path = self.main_image.path.replace('news_images/', 'news_images/previews/')
            img.save(preview_path)
            self.preview_image = preview_path
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Place(models.Model):
    name = models.CharField(max_length=255)
    coordinates = gis_models.PointField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Рейтинг: {self.rating})"


class WeatherReport(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='weather_reports')
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    wind_direction = models.CharField(max_length=50)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    report_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Прогноз погоды для {self.place.name} на {self.report_date}"
