FROM python:3.9

RUN apt-get update && apt-get install -y telnet tcpdump iputils-ping dnsutils

WORKDIR /opt/FinanceApp

COPY . /opt/FinanceApp

COPY db.sqlite3 /opt/db/db.sqlite3

RUN mkdir -p /opt/FinanceApp/static

RUN pip install -r /opt/FinanceApp/requirements.txt

RUN python manage.py collectstatic

RUN python /opt/FinanceApp/manage.py migrate

CMD ["python", "/opt/FinanceApp/manage.py", "runserver", "0.0.0.0:8000"]
