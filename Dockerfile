FROM python:3.5

MAINTAINER Mrcode <mrcodehang@outlook.com>
RUN mkdir -p /app
WORKDIR /app

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ADD . /app
RUN pip install -r requirements.txt

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8888

ENTRYPOINT ["docker-entrypoint.sh"]
