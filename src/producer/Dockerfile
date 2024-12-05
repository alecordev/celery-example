FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY app.py .

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "app.py"]