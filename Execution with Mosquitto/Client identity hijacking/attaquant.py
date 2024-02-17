import paho.mqtt.client as mqtt
import time
broker="localhost"
port =1883
mqttv=mqtt.MQTTv5
client_id="publisher"

def on_log(client, userdata, level, buf):
   print(buf) 

def on_connect(client, userdata, flags, rc, protocol):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
        client.loop_stop()  

mqtt.Client.connected_flag=False#create flag in class

client = mqtt.Client("publisher",protocol=mqttv)             #create new instance

client.username_pw_set(username="publisher",password="123456")

client.on_log=on_log

client.on_connect = on_connect

client.connect(broker,port)           #establish connection

client.loop_start()

while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(200)

client.loop_stop()












