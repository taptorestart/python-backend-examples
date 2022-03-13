import kafka


consumer = kafka.KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(topics=['quickstart-events'])
for msg in consumer:
    print(msg)
