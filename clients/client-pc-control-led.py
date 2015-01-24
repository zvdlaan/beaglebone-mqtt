#! /usr/bin/python

# for demo purposes run from a machine on a different network than
# the beaglebone

import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, msg):
        print( "-- INCOMING MESSAGE --" + "\n\t[topic]: " + msg.topic + "\n\t[message]: " + msg.payload + "\n")

def publish( topic, message ):
	print( "-- PUBLISHING --" )
        global client
	publish_result = client.publish(topic, message)
        #print( "\t[id]: " + str(publish_result[1]) + "\n\t[status]: Attempting to publish" + "\n\t[topic]: " + topic + "\n\t[message]: " + message + "\n")
	print( "\t[topic]: " + topic + "\n\t[message]: " + message + "\n")

# callback for CONNACK response from server.
def on_connect(client, userdata, rc):
	print( "-- CONNECTED --\n")	
	client.subscribe("cis654/mqtt/test/beaglebone/temp")
        print( "-- SUBSCRIBED --" + "\n\t[topic]: cis654/mqtt/test/beaglebone/temp \n")

# callback for PUBLISH message from server
#def on_publish(client, userdata, mid):
#	print( "-- MESSAGE SENT --" + "\n\t[id]:" + str(mid) + "\n\t[status]: Published Successfully \n")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_publish = on_publish

client.connect("iot.eclipse.org", 1883, 60)

# infinite loop
client.loop_start()

while True:
	time.sleep(10)
	publish( "cis654/mqtt/test/beaglebone/led", "on" )
	time.sleep(10)
	publish( "cis654/mqtt/test/beaglebone/led", "off" )
	
