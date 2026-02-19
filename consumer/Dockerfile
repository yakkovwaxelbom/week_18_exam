FROM python:3.11-slim

WORKDIR /app

COPY consumer/requirements.txt .
COPY .env .
COPY consumer/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]