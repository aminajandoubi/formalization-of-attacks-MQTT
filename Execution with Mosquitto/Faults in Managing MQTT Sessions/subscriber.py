import paho.mqtt.client as mqtt
import time
import logging,sys
logging.basicConfig(level=logging.DEBUG)
keepalive=1200
broker="localhost"
port =1883
client_id="subscribe"

def on_log(client, userdata, level, buf):
   print(buf) 

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
        client.loop_stop()  

mqtt.Client.connected_flag=False#create flag in class
CLEAN_SESSION=False
client = mqtt.Client("subscribe",clean_session=CLEAN_SESSION)             #create new instance

client.username_pw_set(username="subscribe",password="123456789")
#mqtt.Client.clean_session=True
client.on_log=on_log

client.on_connect = on_connect

client.connect(broker,port,keepalive)           #establish connection

client.loop_start()

while not client.connected_flag: #wait in loop
    print("In wait loop")
    
client.subscribe("test",0)


client.loop_stop()

client.disconnect()













