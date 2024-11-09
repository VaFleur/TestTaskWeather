# TestTaskWeather

## Описание

Приложение на Django с функционалом:
- CRUD для новостей.
- Редактирование новостей с использованием rich-текста (Django Summernote).
- Периодическая отправка email о новостях с помощью Celery.
- Импорт примечательных мест из xlsx.
- Периодическая задача для получения сводки погоды.
- Экспорт сводки погоды в xlsx-файл.

## Технологии

- Django
- Django REST Framework
- Django Summernote
- Celery + Redis
- PostgreSQL + PostGIS
- Docker

## Установка и запуск

1. Клонируйте репозиторий:
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Запустите Docker-контейнеры:
    ```bash
    docker-compose up --build
    ```

3. Примените миграции:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. Создайте суперпользователя:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5. Откройте приложение в браузере:
    ```
    http://localhost:8000
    ```
