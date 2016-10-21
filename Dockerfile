FROM python:3.5

MAINTAINER Mrcode <mrcodehang@outlook.com>

RUN python -m pip install sanic

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8888

ENTRYPOINT ["docker-entrypoint.sh"]

CMD [""]