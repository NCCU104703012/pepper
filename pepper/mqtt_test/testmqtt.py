# SubscriberTest.py
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("TOPIC01")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    global num
    num = str(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("140.119.163.193", 1883, 60)
client.loop_forever()
