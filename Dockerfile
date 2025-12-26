FROM python:3.12-slim

ENV FLASK_APP=flasky.py
ENV FLASK_CONFIG=docker
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app app
COPY migrations migrations
COPY flasky.py config.py boot.sh ./
RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
