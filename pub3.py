###Sensor 3

#import paho.mqtt.client
import paho.mqtt.client as mqtt
#import random to generate random value
from random import uniform
#import time to sleep/delay
import time

#set public mqtt broker
mqttBroker = 'broker.emqx.io'
#set client name
sensor3 = mqtt.Client("Sensor 3")
#connect to public broker
sensor3.connect(mqttBroker)
#always run the sensor
sensor3.loop_start()
while True:	
	#generate random number as a temperature		
	randNumber = uniform(22.0, 27.0)
	#publish a topic to broker
	sensor3.publish("Sensor 3", round(randNumber,2))
	#print ouput
	print("Suhu: "+ str(round(randNumber,2))+ " derajat celcius")
	#delay 10 second
	time.sleep(10)