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
    git clone https://github.com/VaFleur/TestTaskWeather
    cd ./TestTaskWeather
    ```

2. Запустите Docker-контейнеры:
    ```bash
    docker compose up --build
    ```

3. Примените миграции:
    ```bash
    docker compose exec web python manage.py migrate
    ```

4. Создайте суперпользователя:
    ```bash
    docker compose exec web python manage.py createsuperuser
    ```

5. Откройте приложение в браузере:
    ```
    http://localhost:8000
    ```
## Импорт из xlsx

Файл должен иметь колонки:

- Название места
- Широта
- Долгота
- Рейтинг

Импорт осуществляется командой:
   ```
    python manage.py import_places path/to/your/file.xlsx
   ```
## Экспорт сводки погоды в xlsx

Вы можете экспортировать сводку погоды в xlsx-файл с фильтрацией по Примечательному месту и дате через специальный API-эндпоинт.
   ```
   GET http://localhost:8000/api/export-weather/?place=<Название_места>&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
   ```

- place (необязательно): Название Примечательного места, по которому будет происходить фильтрация.
- start_date (необязательно): Дата начала диапазона (включительно), формат YYYY-MM-DD.
- end_date (необязательно): Дата окончания диапазона (включительно), формат YYYY-MM-DD.

Пример:
   ```
   http://localhost:8000/api/export-weather/?place=Красноярск&start_date=2024-01-01&end_date=2024-11-30
   ```
После выполнения запроса, вы получите файл weather_report.xlsx с отфильтрованными данными.