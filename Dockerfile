FROM python:3.5

MAINTAINER Mrcode <mrcodehang@outlook.com>
RUN mkdir -p /app
WORKDIR /app

RUN python -m pip --default-timeout=100 install sanic

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ADD /app .

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8888

ENTRYPOINT ["docker-entrypoint.sh"]
#RUN python entry.py
CMD [""]