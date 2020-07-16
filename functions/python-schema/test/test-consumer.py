import pulsar

from pulsar.schema import *


class Person(Record):
    name = String()
    phone = String()


client = pulsar.Client('pulsar://127.0.0.1:6650')

consumer = client.subscribe(topic='persistent://public/default/out', subscription_name='ew', schema=AvroSchema(Person))

while True:
    msg = consumer.receive()
    ex = msg.value()
    try:
        print("Received message name={} phone={}".format(ex.name, ex.phone))
        # Acknowledge successful processing of the message
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()
