FROM python:alpine

RUN apk add gcc libc-dev
RUN pip install kafka-python happybase

RUN mkdir /srv/kafka-messages-to-hbase
WORKDIR /srv/kafka-messages-to-hbase
COPY start.py ./

CMD ["python", "./start.py"]