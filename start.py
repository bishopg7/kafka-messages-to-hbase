import logging, os, sys, uuid, happybase
from kafka import KafkaConsumer

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

bootstrap_servers = os.environ["KAFKA_SERVERS"]
topic = os.environ["KAKFA_TOPIC"]
group_id = os.environ["KAFKA_GROUP_ID"]
auto_offset_reset  = os.environ["KAFKA_OFFSET_RESET"]

hbase_thrift_host = os.environ["HBASE_THRIFT_HOST"]
hbase_thrift_port = int(os.environ["HBASE_THRIFT_PORT"])
hbase_table = os.environ["HBASE_TABLE"]


def msg_to_hbase():
    consumer = KafkaConsumer(topic,
                             group_id=group_id,
                             bootstrap_servers=bootstrap_servers,
                             auto_offset_reset=auto_offset_reset,
                             enable_auto_commit=True,
                             max_poll_records=5000,
                             fetch_max_wait_ms=1000
                             )

    hbase_thrift_connection = happybase.Connection(host=hbase_thrift_host,
                                                   port=hbase_thrift_port
                                                   )
    table = hbase_thrift_connection.table(hbase_table)

    for message in consumer:
        msg_str = message.value.decode('utf-8')
        msg_list = msg_str.split(";")
        table.put(uuid.uuid4().hex,
                  {b'data:shortLink': msg_list[0],
                  b'data:ts': msg_list[1],
                  b'data:channel': msg_list[2],
                  b'data:price': msg_list[3],
                  b'data:longLink': msg_list[4]}
                  )
    hbase_thrift_connection.close()

msg_to_hbase()
