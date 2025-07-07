FROM python:3.9-alpine

WORKDIR /app

# התקנת כלים ותלויות לבניית mysqlclient
RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    libffi-dev \
    && pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY static/ static/
COPY templates/ templates/
COPY app.py dbcontext.py person.py ./

EXPOSE 8080
ENTRYPOINT ["python", "app.py"]

