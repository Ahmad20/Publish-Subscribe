import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

#mqttBroker = 'mqtt.eclipseprojects.io'
mqttBroker = 'broker.emqx.io'
#mqttBroker = 'test.mosquitto.org'
#mqttBroker = '26.140.129.33'
#mqttBroker = "localhost"
client = mqtt.Client("Sensor 1")
client.connect(mqttBroker)
client.loop_start()
while True:	
	randNumber = uniform(25.0, 30.0)
	client.publish("Sensor 1", round(randNumber,2))
	print("Suhu: "+ str(round(randNumber,2))+ " derajat celcius")
	time.sleep(10)
