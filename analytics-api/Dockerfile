FROM python:3.11-slim

WORKDIR /app

COPY ./analytics-api/requirements.txt .
COPY .env .
COPY ./analytics-api/ .


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
