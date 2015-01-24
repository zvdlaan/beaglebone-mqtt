#! /usr/bin/python

import Beaglebone_PWM as PWM

pwmPin = 'P9_14'
rc_init = PWM.InitializePin(pwmPin)
PWM.SetFrequency(pwmPin, 60)

