import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 
import time
import logging,sys
logging.basicConfig(level=logging.DEBUG)
keepalive=1200
broker="localhost"
port =1883
client_id="publisher"

def on_log(client, userdata, level, buf):
   print(buf) 

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
        client.loop_stop()  

def on_disconnect(client, userdata, rc):
   print("client disconnected ok")

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= "  ,mid)

mqtt.Client.connected_flag=False#create flag in class
client = mqtt.Client("publisher")             #create new instance

client.username_pw_set(username="publisher",password="123456")
client.on_log=on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.connect(broker,port,keepalive)           #establish connection
client.loop_start()
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(3)
ret=client.publish('test',"Test message",0)    #publish
time.sleep(5)
ret1=client.publish('test',"Test message",0)    #publish
time.sleep(5)
ret3=client.publish('test',"Test message",0)    #publish
time.sleep(5)
#print("published return=",ret)
client.loop_stop()













