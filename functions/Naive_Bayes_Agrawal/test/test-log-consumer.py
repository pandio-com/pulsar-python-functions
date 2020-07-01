import pulsar, json

client = pulsar.Client('pulsar://127.0.0.1:6650')

consumer = client.subscribe(topic='persistent://public/default/log', subscription_name='log', consumer_type=pulsar.ConsumerType.Shared)

while True:
    msg = consumer.receive()
    try:
        print("Received message '{}' id='{}'".format(msg.value(), msg.message_id()))

        # Acknowledge successful processing of the message
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()