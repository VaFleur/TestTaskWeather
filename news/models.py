from django.db import models
from django.contrib.gis.db import models as gis_models
from PIL import Image


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
