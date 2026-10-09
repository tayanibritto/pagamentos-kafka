import json
from kafka import KafkaProducer
from app.config import settings

# Cria conexão com o broker Kafka
producer = KafkaProducer(
    bootstrap_servers=settings.kafka_bootstrap_servers,
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

# Função para receber evento e publicar no tópico configurado
def send_payment_event(event: dict) -> None:
    producer.send(
        settings.kafka_topic,
        value=event
    )

    producer.flush()