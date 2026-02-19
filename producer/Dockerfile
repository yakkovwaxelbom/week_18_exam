FROM python:3.11-slim

WORKDIR /app

COPY producer/requirements.txt .
COPY .env .
COPY data/ .
COPY producer/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
