import paho.mqtt.client as mqtt
import time

val=[]
def on_message(client, userdata, message):
	a = float(message.payload.decode("utf-8"))
	print("Received Message: ", round(a,2), " From ", message.topic)
	val.append(a)
	if len(val)>3:
		del val[:]
		val.append(a)
	avg = round(sum(val)/len(val),2)
	print(val)
	print("Average:", avg)
	
#mqttBroker = 'mqtt.eclipseprojects.io'
mqttBroker = 'broker.emqx.io'
#mqttBroker = 'test.mosquitto.org'
#mqttBroker = '26.140.129.33'
#https://www.hivemq.com/public-mqtt-broker/
client = mqtt.Client("Client1")
client.on_message = on_message
client.connect(mqttBroker)

client.loop_start()

while True:
	time.sleep(1)
	client.subscribe("Sensor 1")
	#time.sleep(1)
	client.subscribe("Sensor 2")
	#time.sleep(1)
	client.subscribe("Sensor 3")
client.loop_stop()