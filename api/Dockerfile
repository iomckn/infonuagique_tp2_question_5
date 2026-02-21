FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV PORT=3000
EXPOSE 3000

# Gunicorn = plus “prod-ready” qu’un serveur Flask dev
CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app", "--workers", "2", "--threads", "4"]
