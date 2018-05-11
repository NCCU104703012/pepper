import paho.mqtt.client as mqtt
import json
# Define Variables
MQTT_HOST = "192.168.0.10"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "sensor/test"

def on_connect(client, userdata, flags, rc):
    print "Connected"
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    #print(msg.topic)
    #print(msg.payload) # <- do you mean this payload = {...} ?
    payload = json.loads(msg.payload) # you can use json.loads to convert string to json
    RShoulderPitch = payload['RShoulderPitch']
    RShoulderRoll = payload['RShoulderRoll']
    LShoulderPitch = payload['LShoulderPitch']
    LShoulderRoll = payload['LShoulderRoll']
    RElbowYaw = payload['RElbowYaw']
    RElbowRoll = payload['RElbowRoll']
    LElbowYaw = payload['LElbowYaw']
    LElbowRoll = payload['LElbowRoll']

    #print(payload['check']) # then you can check the value
    #if payload['check']=="one":
    #    print(payload['token1'])
    #    client.disconnect()
    #print(json.dumps(payload, indent=4))
    print(RShoulderPitch,RShoulderRoll)
    print(LShoulderPitch,LShoulderRoll)
    print(RElbowYaw,RElbowRoll)
    print(LElbowYaw,LElbowRoll)
    #client.disconnect() # Got message then disconnect

# Initiate MQTT Client
mqttc = mqtt.Client()

mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

print("end connect")
mqttc.loop_forever()
print("end loop")