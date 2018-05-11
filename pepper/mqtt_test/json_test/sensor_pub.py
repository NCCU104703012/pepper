#coding=utf-8

import paho.mqtt.client as mqtt
import json
# Define Variables
MQTT_HOST = "192.168.0.10"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "sensor/test"



output = {}
RShoulderPitch = "RShoulderPitch"
RShoulderRoll = "RShoulderRoll"
LShoulderPitch = "LShoulderPitch"
LShoulderRoll = "LShoulderRoll"
RElbowYaw = "RElbowYaw"
RElbowRoll = "RElbowRoll"
LElbowYaw = "LElbowYaw"
LElbowRoll = "LElbowRoll"

'''
RShoulderPitch 上下 -119.5 to 119.5
RShoulderRoll 側邊開合 -89.5 to -0.5
LShoulderPitch -119.5 to 119.5
LShoulderRoll 	0.5 to 89.5
RElbowYaw 轉動  -119.5 to 119.5
RElbowRoll 屈伸  0.5 to 89.5
LElbowYaw 	-119.5 to 119.5
LElbowRoll	-89.5 to -0.5
'''
output['RShoulderPitch'] = RShoulderPitch
output['RShoulderRoll'] = RShoulderRoll
output['LShoulderPitch'] = LShoulderPitch
output['LShoulderRoll'] = LShoulderRoll
output['RElbowYaw'] = RElbowYaw
output['RElbowRoll'] = RElbowRoll
output['LElbowYaw'] = LElbowYaw
output['LElbowRoll'] = LElbowRoll

output = json.dumps(output)

def on_publish(client, userdata, mid):
    print "Message Published..."


# Initiate MQTT Client
mqttc = mqtt.Client()

mqttc.on_publish = on_publish

mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

while 1 :
    name = raw_input('Enter input:')
    if name=="1" :
        mqttc.publish(MQTT_TOPIC, output)
