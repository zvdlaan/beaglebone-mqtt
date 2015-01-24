#! /usr/bin/python

import paho.mqtt.client as mqtt
import time

import sys
sys.path.insert(0, '/home/vandy/Code/mqtt-beaglebone/bbb-python-io')
import BBB_ADC as ADC
ADC.Initialize()

# callback for CONNACK response from server
def on_connect(client, userdata, rc):
	print( "-- CONNECTED --\n")
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("cis654/mqtt/test/beaglebone/led")	
	print( "-- SUBSCRIBED --" + "\n\t[topic]: cis654/mqtt/test/beaglebone/led \n")
        

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
#	print( "-- INCOMING MESSAGE --" + "\n\t[topic]: " + msg.topic + "\n\t[message]: " + str(msg.payload) + "\n" )
	""" blah """

def publish( topic, message ):
	print( "-- PUBLISHING --" )
        global client
	publish_result = client.publish(topic, message)
        #print( "\t[id]: " + str(publish_result[1]) + "\n\t[status]: Attempting to publish" + "\n\t[topic]: " + topic + "\n\t[message]: " + str(message))
	print( "\t[topic]: " + topic + "\n\t[message]: " + str(message) + "\n" )


# callback for PUBLISH after mesage is successfully sent to server
#def on_publish(client, userdata, mid):
#	print( "-- MESSAGE SENT --" + "\n\t[id]:" + str(mid) + "\n\t[status]: Published Successfully \n")



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_publish = on_publish

client.connect("iot.eclipse.org", 1883, 60)
#client.connect("messagesight.demos.ibm.com", 1883, 60)
client.loop_start()

while True:
	time.sleep(15)
	millivolts = ADC.GetValueMillivolts( 'P9-40' )
        temp_c = (float(millivolts) - 500) / 10
        temp_f = (temp_c * 9/5) + 32
	publish( "cis654/mqtt/test/beaglebone/temp", temp_f )
