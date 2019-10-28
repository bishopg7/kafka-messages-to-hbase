App in docker which reads messages from kafka's topic splited ";" and writes some data in hbase table via thrift server. 
Reqired running hbase thrift server.

Build & run:
~~~~
docker build . -t kafka-messages-to-hbase
docker run -d --env-file=env.list kafka-messages-to-hbase
~~~~

example message in kafka's topic:
~~~~
cnMqU2S;1571910386260;XXXX;YYYY;mayor/themes/18299/5698050/
tP1dfOy;1571732580266;ХХХХ;YYYY;services/catalog
~~~~