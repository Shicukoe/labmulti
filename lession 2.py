print("MQTT with Adafruit IO")
import sys
import time
import random
import requests
from Adafruit_IO import MQTTClient

AIO_USERNAME = "Tus"
AIO_KEY = "aio_oKKH41A4UMBkoRqe5OpKnbCsqf3s"

global_equation = " x1 + x2 + x3  "

def init_global_equation():
    headers = {}
    aio_url = "https://io.adafruit.com/api/v2/Tus/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()
    global_equation = data["last_value"]
    print("Get lastest value:", global_equation)

def modify_value(x1, x2, x3):
    result = eval(global_equation)
    print(result)
    return result

def connected(client):
    print("Server connected ...")
    client.subscribe("button1")
    client.subscribe("button2")
    client.subscribe("equation")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribed!!!")

def disconnected(client):
    print("Disconnected from the server!!!")
    sys.exit (1)


def message(client , feed_id , payload):
    print("Received: " + payload)
    if(feed_id == "equation"):
        global_equation = payload
        print(global_equation)


client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.on_connect = connected  #function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()
init_global_equation()

while True:
    time.sleep(5)
    value1 =random.randint(20,70)
    value2 =random.randint(0,100)
    value3 =random.randint(0,1000)
    print("updating...")
    client.publish("sensor1",value1)
    client.publish("sensor2",value2)
    client.publish("sensor3",value3)
    value4 = modify_value(value1, value2, value3)
    print(value4)  
    pass