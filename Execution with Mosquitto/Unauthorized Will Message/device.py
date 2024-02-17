import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 
import time
broker="localhost"
port =1883
mqttv=mqtt.MQTTv5
kep=60
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

mqtt.Client.connected_flag=False#create flag in class
client = mqtt.Client("subscriber",protocol=mqttv)             #create new instance
client.username_pw_set(username="subscriber",password="12345687")
client.will_set(topic = "test", payload="bonjour", qos=0,retain=True)
client.on_log=on_log
client.on_connect = on_connect
client.connect(broker,port,keepalive=kep)           #establish connection
client.loop_start()
while not client.connected_flag: #wait in loop
    print("In wait loop")

time.sleep(10)
client.loop_stop()
