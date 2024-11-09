from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from constance import config
from .models import News, Place, WeatherReport
import requests


@shared_task
def send_daily_news_email():
    today = timezone.now().date()
    news_today = News.objects.filter(publication_date=today)

    if news_today.exists():
        news_list = '\n'.join([f'{news.title}: {news.content[:100]}...' for news in news_today])
        email_body = f"{config.NEWS_EMAIL_BODY}\n\n{news_list}"

        send_mail(
            config.NEWS_EMAIL_SUBJECT,
            email_body,
            'noreply@yourdomain.com',
            config.NEWS_RECIPIENTS,
            fail_silently=False,
        )


API_KEY = '8800c729db107fa71931fec4cce6bb59'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'


@shared_task
def fetch_weather_data():
    places = Place.objects.all()
    for place in places:
        lat, lon = place.coordinates.y, place.coordinates.x
        response = requests.get(
            WEATHER_URL,
            params={'lat': lat, 'lon': lon, 'appid': API_KEY, 'units': 'metric'}
        )

        if response.status_code == 200:
            data = response.json()

            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind_speed = data['wind']['speed']
            wind_direction = data['wind'].get('deg', 'N/A')

            WeatherReport.objects.create(
                place=place,
                temperature=temperature,
                humidity=humidity,
                pressure=pressure,
                wind_speed=wind_speed,
                wind_direction=wind_direction,
                report_date=timezone.now()
            )
        else:
            print(f"Failed to fetch weather data for {place.name}")
