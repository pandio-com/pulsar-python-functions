import pulsar

from pulsar.schema import *


class Person(Record):
    name = String()
    phone = String()


client = pulsar.Client('pulsar://127.0.0.1:6650')

producer = client.create_producer(topic='persistent://public/default/in', schema=AvroSchema(Person))
producer.send(Person(name='Josh Eric', phone='616-402-0625'))

client.close()
