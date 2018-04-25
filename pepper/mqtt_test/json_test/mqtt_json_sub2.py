import paho.mqtt.client as mqtt
import json
# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "irisPayload"

def on_connect(client, userdata, flags, rc):
    print "Connected"
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    #print(msg.topic)
    #print(msg.payload) # <- do you mean this payload = {...} ?
    payload = json.loads(msg.payload) # you can use json.loads to convert string to json
    print(payload['check']) # then you can check the value
    if payload['check']=="one":
        print(payload['token1'])
        client.disconnect()
    #print(json.dumps(payload, indent=4))
    #client.disconnect() # Got message then disconnect

# Initiate MQTT Client
mqttc = mqtt.Client()

mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

print("end connect")
mqttc.loop_forever()
print("end loop")
