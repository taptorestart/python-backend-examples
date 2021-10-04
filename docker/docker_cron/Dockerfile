FROM python:3.8-buster

WORKDIR /home/app

RUN apt-get update
RUN apt-get install -y cron
COPY . /home/app
COPY crontab-example /etc/cron.d/crontab-example

RUN chmod 0644 /etc/cron.d/crontab-example
RUN crontab /etc/cron.d/crontab-example
CMD ["cron", "-f"]
