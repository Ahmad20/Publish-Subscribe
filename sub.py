###Client

#import paho.mqtt.client
import paho.mqtt.client as mqtt
#import time to sleep/delay
import time

#set empty list to save current temperature
val=[]
#on_message function
def on_message(client, userdata, message):
	#get the message and cast to float64
	msg = float(message.payload.decode("utf-8"))
	#print output
	print("Received Message: ", round(msg,2), " From ", message.topic)
	#append message(temperature) to list
	val.append(msg)
	#set list empty when have 3 value
	if len(val)>3:
		del val[:]
		val.append(msg)
	#get the average by divided with number of message on list
	avg = round(sum(val)/len(val),2)
	#output the list
	print(val)
	#output the average
	print("Average:", avg)
	
#set public mqtt broker
mqttBroker = 'mqtt.eclipseprojects.io'
#set client name
client = mqtt.Client("Client1")
#set function on_message
client.on_message = on_message
#connect to public broker
client.connect(mqttBroker)

#always run the client
client.loop_start()
while True:
	#delay 1 second
	time.sleep(1)
	#subscribe to sensor 1, sensor 2, sensor 3 with QOS=2
	client.subscribe([("Sensor 1", 2), ("Sensor 2", 2), ("Sensor 3", 2)])

	
