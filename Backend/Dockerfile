# Используйте базовый образ Docker для Python с поддержкой Django
FROM python:3.9

# Установите рабочую директорию
WORKDIR /opt/FinanceApp

# Скопируйте файлы приложения в образ
COPY . /opt/FinanceApp

# Копируйте файл db.sqlite3 в /opt/db
COPY db.sqlite3 /opt/db/db.sqlite3

# Создайте директорию static
RUN mkdir -p /opt/FinanceApp/static

# Установите зависимости из файла requirements.txt
RUN pip install -r /opt/FinanceApp/requirements.txt

RUN python manage.py collectstatic

# Выполните миграции базы данных
RUN python /opt/FinanceApp/manage.py migrate

# Запустите сервер Django
CMD ["python", "/opt/FinanceApp/manage.py", "runserver", "0.0.0.0:8000"]
