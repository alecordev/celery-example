FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY tasks.py .

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]