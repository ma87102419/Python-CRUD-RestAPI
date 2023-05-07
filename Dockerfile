FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
COPY init-employeedb.sql /docker-entrypoint-initdb.d/init-employeedb.sql
RUN sed -i 's/\r$//g' /docker-entrypoint-initdb.d/init-employeedb.sql

CMD ["python", "app.py"]
