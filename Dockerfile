FROM python:3.5

MAINTAINER Mrcode <mrcodehang@outlook.com>
WORKDIR /var/www/cqut/chat-server/

RUN python -m pip install sanic

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ADD entry.py /var/www/cqut-chat-server/entry.py

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8888

ENTRYPOINT ["docker-entrypoint.sh"]
#RUN python entry.py
CMD [""]