import pulsar, json

client = pulsar.Client('pulsar://127.0.0.1:6650')

producer = client.create_producer('persistent://public/default/in')
producer.send(json.dumps({'phone': '6164020025'}).encode('utf8'))

client.close()