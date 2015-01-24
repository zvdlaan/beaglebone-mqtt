#!/usr/bin/python


import sys
sys.path.insert(0, '/home/vandy/Code/mqtt-beaglebone/bbb-python-io')
import BBB_ADC as ADC

import time

ADC.Initialize()

while True:	
	millivolts = ADC.GetValueMillivolts( 'P9-40' )
	temp_c = (float(millivolts) - 500) / 10
	temp_f = (temp_c * 9/5) + 32
	print temp_f
	time.sleep(2)	
	




