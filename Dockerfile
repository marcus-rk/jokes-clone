FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

# command to run on container start. gunicorn is a WSGI HTTP server
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]