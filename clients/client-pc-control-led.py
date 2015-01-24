#! /usr/bin/python

# for demo purposes run from a machine on a different network than
# the beaglebone

import paho.mqtt.client as mqtt
import time

def publish( topic, message ):
	print( "-- PUBLISHING --" )
        global client
	publish_result = client.publish(topic, message)
        print( "\t[id]: " + str(publish_result[1]) + "\n\t[status]: Attempting to publish" + "\n\t[topic]: " + topic + "\n\t[message]: " + message)

# callback for CONNACK response from server.
def on_connect(client, userdata, rc):
	print( "-- CONNECTED --\n")

# callback for PUBLISH message from server
def on_publish(client, userdata, mid):
	print( "-- MESSAGE SENT --" + "\n\t[id]:" + str(mid) + "\n\t[status]: Published Successfully \n")


client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

client.connect("iot.eclipse.org", 1883, 60)

# infinite loop
client.loop_start()

while True:
	time.sleep(2)
	publish( "cis654/mqtt/test/beaglebone/led", "on" )
	time.sleep(2)
	publish( "cis654/mqtt/test/beaglebone/led", "off" )
	



