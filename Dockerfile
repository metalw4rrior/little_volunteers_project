FROM python:3.10-slim

RUN apt-get update && apt-get install -y sqlite3

WORKDIR /app

COPY . /app

CMD ["python", "main.py"]
