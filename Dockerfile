FROM python:3.10-bullseye

# Use the flask dir as the working dir
WORKDIR /app

RUN apt-get update && \
    apt-get -y install cron iputils-ping

COPY ./flask_app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP app.py
ENV FLASK_RUN_PORT 5001
ENV FLASK_RUN_HOST 0.0.0.0

# Health check for background running cron
HEALTHCHECK --interval=1m --timeout=3s CMD ps -e | grep cron | grep -v "defunct"

CMD ["bash","-c","crontab /cron_data/crontab && cron && flask run"]
