
import sys
from Adafruit_IO import Client
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *
from uart import *

AIO_FEED_IDs = ["button1", "button2"]
AIO_USERNAME = "thanhliemtala"
AIO_KEY = "aio_gyUv68VsDq0FC34RFu99SsYdcfEz"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)



client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
#client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
counter_ai = 3
timer = 0
ai_result = ""
previous_result = ""
while True:
   # counter = counter - 1
  #  if counter <= 0:
   #        counter = 10
            #TODO
    #        print("Random data is publising")
    #        temp = random.randint(10,60)
     #       client.publish("cambien1", temp)
     #       light = random.randint(0,500)
      #      client.publish("cambien2", light)
      #      humi = random.randint(0,100)
       #     client.publish("cambien3", humi)
    counter_ai = counter_ai - 1
    if counter_ai <=0:
        counter_ai = 3
        previous_result = ai_result
        ai_result = image_detector()
        print("AI Output: ", ai_result)
        if previous_result != ai_result:
            client.publish("ai", ai_result)
            print("AI Output: ", ai_result)
    readSerial(client)
    time.sleep(1)
    pass