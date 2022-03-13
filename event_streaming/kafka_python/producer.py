import kafka


producer = kafka.KafkaProducer(bootstrap_servers='localhost:9092')
future = producer.send(topic='quickstart-events', key=b'foo', value=b'bar')
result = future.get(timeout=60)
