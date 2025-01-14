import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage

BROKER, PORT = "127.0.0.1", 1883

def on_message(client, userdata, msg):
    print(f'Received {msg.payload.decode()}')

def on_connection(client, userdata, flag, rc):
    if rc==0:
        print("connected OK Returned code ", rc)
    else:
        print("Bad connection Returned code= ", rc)

client = paho.Client()
client.on_message = on_message
client.on_connect = on_connection
client.connect(BROKER, PORT)
client.subscribe("display")
client.loop_forever()
