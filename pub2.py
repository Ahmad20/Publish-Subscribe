###Sensor 2

#import paho.mqtt.client
import paho.mqtt.client as mqtt
#import random to generate random value
from random import uniform
#import time to sleep/delay
import time

#set public mqtt broker
mqttBroker = 'broker.emqx.io'
#set client name
sensor2 = mqtt.Client("Sensor 2")
#connect to public broker
sensor2.connect(mqttBroker)
#always run the sensor
sensor2.loop_start()
while True:	
	#generate random number as a temperature	
	randNumber = uniform(20.0, 25.0)
	#publish a topic to broker
	sensor2.publish("Sensor 2", round(randNumber,2))
	#print ouput
	print("Suhu: "+ str(round(randNumber,2))+ " derajat celcius")
	#delay 10 second
	time.sleep(10)