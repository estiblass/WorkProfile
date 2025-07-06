FROM python:3.11-slim

# התקנת תלויות מערכת עבור mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app.py dbcontext.py person.py requirements.txt ./
COPY templates/ templates/
COPY static/ static/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
