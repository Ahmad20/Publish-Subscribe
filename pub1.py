###Sensor 1

#import paho.mqtt.client
import paho.mqtt.client as mqtt
#import random to generate random value
from random import uniform
#import time to sleep/delay
import time

#set public mqtt broker
mqttBroker = 'broker.emqx.io'
#set client name
sensor1 = mqtt.Client("Sensor 1")
#connect to public broker
sensor1.connect(mqttBroker)
#always run the sensor
sensor1.loop_start()
###3a
a=[]
while True:
	#generate random number as a temperature	
	randNumber = uniform(25.0, 30.0)
	#publish a topic to broker
	sensor1.publish("Sensor 1", round(randNumber,2))
	#print ouput
	print("Suhu: "+ str(round(randNumber,2))+ " derajat celcius")
	#delay 10 second
	time.sleep(10)