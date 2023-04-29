import paho.mqtt.client as mqtt
broker = 'broker.emqx.io'
print('start of program 2')
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe('colabtry')

# when receiving a mqtt message do this;

def on_message(client, userdata, msg):
	message = str(msg.payload)
	print(msg.topic+" "+message)
    

def on_publish(mosq, obj, mid):
	print("mid: " + str(mid))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.publish("wslmqtt", "alive")
client.loop_forever()


