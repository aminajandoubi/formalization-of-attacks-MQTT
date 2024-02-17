import paho.mqtt.client as mqtt
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
client.username_pw_set(username="subscriber",password="1234568888")

client.on_log=on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.connect(broker,port)           #establish connection

client.loop_start()

while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(3)
client.subscribe("test")
time.sleep(100)

client.loop_stop()

client.disconnect()












