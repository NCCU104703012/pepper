import paho.mqtt.client as mqtt
import json
# Define Variables
MQTT_HOST = "140.119.163.193"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "irisPayload"

MQTT_MSG=json.dumps({"sepalLength": "6.4","sepalWidth":  "3.2","petalLength": "4.5","petalWidth":  "1.5"});

def on_publish(client, userdata, mid):
    print "Message Published..."


# Initiate MQTT Client
mqttc = mqtt.Client()

mqttc.on_publish = on_publish

mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

while 1 :
    name = raw_input('Enter input:')
    mqttc.publish(MQTT_TOPIC, MQTT_MSG)
