#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os
import logging

# enable logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d.%m. %I:%M:%S %p',filename='/var/log/openhab/pir.log',level=logging.INFO)

# REST url to POST commands
rest_url = "http://192.168.0.100:8080/rest/items/PIR_WZ"

GPIO.setmode(GPIO.BCM)
PIR_PIN = 18                     # this is the GPIO pin
GPIO.setup(PIR_PIN, GPIO.IN)
def motion(PIR_PIN):
	os.system("/usr/bin/curl --header \"Content-Type: text/plain\" --request POST --data \"ON\" " + rest_url)
	logging.info("motion  ON: " + rest_url)
	time.sleep(5)
	os.system("/usr/bin/curl --header \"Content-Type: text/plain\" --request POST --data \"OFF\" " + rest_url)
	os.system("/usr/bin/curl --header \"Content-Type: text/plain\" --request POST --data \"OFF\" " + rest_url)
	logging.info("motion OFF: " + rest_url)
	time.sleep(2)

logging.info("Start pirsensor ...")
try:
	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motion)
	while 1:
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
