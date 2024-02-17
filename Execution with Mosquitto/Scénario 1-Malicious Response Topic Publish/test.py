import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 
import time
broker="localhost"
port =1883
mqttv=mqtt.MQTTv5
client_id="subscriber"

def on_log(client, userdata, level, buf):
   print(buf)

def on_connect(client, userdata, flags, rc, protocol):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
        client.loop_stop()  

def on_disconnect(client, userdata, rc, protocol):
   print("client disconnected ok")

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= "  ,mid)

mqtt.Client.connected_flag=False#create flag in class
client = mqtt.Client("subscriber",protocol=mqttv)             #create new instance
client.username_pw_set(username="subscriber",password="12345687")
client.on_log=on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.connect(broker,port)           #establish connection
client.loop_start()
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
time.sleep(3)
client.subscribe("client")
time.sleep(3)
print("publishing")
#déclaration des proporites publish 1
properties=Properties(PacketTypes.PUBLISH) 
properties.ResponseTopic='client'
count=250
properties.CorrelationData=bytes([count])
   
ret=client.publish('test',"Test message",0,properties=properties)    #publish
print("published return=",ret)
time.sleep(4)
#déclaration des proporites publish 2
x=properties.CorrelationData=bytes([count])
response_topic=properties.ResponseTopic='client'
print("publishing")
ret1=client.publish(response_topic,payload=x, properties=None)   #publish
print("published return=",ret1)

time.sleep(4)
client.loop_stop()
print("Correlation_Data =",properties.CorrelationData)
client.disconnect()
