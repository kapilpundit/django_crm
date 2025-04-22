FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: install mysql client system deps
RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc

COPY . .
