# Generated by Django 5.1.3 on 2024-11-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('main_image', models.ImageField(upload_to='news_images/')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='news_images/previews/')),
                ('content', models.TextField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
