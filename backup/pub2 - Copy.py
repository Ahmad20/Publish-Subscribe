import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

#mqttBroker = 'mqtt.eclipseprojects.io'
mqttBroker = 'broker.emqx.io'
#mqttBroker = 'test.mosquitto.org'
#mqttBroker = '26.107.43.179'
#mqttBroker = "localhost"
client = mqtt.Client("Sensor 2")
client.connect(mqttBroker)
client.loop_start()
while True:	
	randNumber = uniform(20.0, 25.0)
	client.publish("Sensor 2", round(randNumber,2))
	print("Suhu: "+ str(round(randNumber,2))+ " derajat celcius")
	time.sleep(10)
