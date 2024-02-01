import paho.mqtt.client as mqtt
import time
import random
import json

broker_address = "localhost"
port = 1883
topics = ["pod1", "pod2", "pod3", "pod4"]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client("MQTT_Producer")
client.on_connect = on_connect

client.connect(broker_address, port=port)

try:
    while True:
        for topic in topics:
            message = {"value": random.randint(0, 100)}
            client.publish(topic, json.dumps(message))
            print(f"Published to {topic}: {message}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Script stopped by user")

client.disconnect()
