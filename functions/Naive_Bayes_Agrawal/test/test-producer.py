import pulsar, json, numpy
from skmultiflow.data import AGRAWALGenerator

client = pulsar.Client('pulsar://127.0.0.1:6650')

producer = client.create_producer('persistent://public/default/in')

generator = AGRAWALGenerator()

while generator.has_more_samples():
    X, Y = generator.next_sample()
    producer.send(json.dumps({'X': X.tolist(), 'Y': Y.tolist()}).encode('utf8'))

client.close()