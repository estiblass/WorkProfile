FROM python:3.9-slim

WORKDIR /app

COPY app.py dbcontext.py person.py requirements.txt ./
COPY templates/ templates/
COPY static/ static/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
