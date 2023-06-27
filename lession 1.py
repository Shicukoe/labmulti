print("MQTT with Adafruit IO")
import sys
import time
import random
from Adafruit_IO import MQTTClient

AIO_USERNAME = "Tus"
AIO_KEY = "aio_BBJn05CdEugwd5Jvo0nPl5523t6M"

def connected(client):
    print("Server connected ...")
    client.subscribe("button1")
    client.subscribe("button2")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribed!!!")

def disconnected(client):
    print("Disconnected from the server!!!")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Received: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.on_connect = connected  #function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

while True:
    time.sleep(5)
    value1 =random.randint(20,70)
    value2 =random.randint(0,100)
    value3 =random.randint(0,1000)
    print("updating...")
    client.publish("sensor1",value1)
    client.publish("sensor2",value2)
    client.publish("sensor3",value3)    
    pass