from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from constance import config
from .models import News


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
