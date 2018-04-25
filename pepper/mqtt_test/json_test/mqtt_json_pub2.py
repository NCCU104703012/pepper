import paho.mqtt.client as mqtt
import json
# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "irisPayload"

MQTT_MSG=json.dumps({"check": "one","token1":  "get token1","petalLength": "4.5","petalWidth":  "1.5"});
MQTT_MSG2=json.dumps({"check": "two","token2":  "get token2","petalLength": "4.5","petalWidth":  "1.5"});

def on_publish(client, userdata, mid):
    print "Message Published..."


# Initiate MQTT Client
mqttc = mqtt.Client()

mqttc.on_publish = on_publish

mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

while 1 :
    name = raw_input('Enter input:')
    if name=="1" :
        mqttc.publish(MQTT_TOPIC, MQTT_MSG)
    if name=="2" :
        mqttc.publish(MQTT_TOPIC, MQTT_MSG2)

    #mqttc.publish(MQTT_TOPIC, MQTT_MSG)
