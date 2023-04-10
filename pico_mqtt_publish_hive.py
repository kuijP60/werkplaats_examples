from machine import Pin
import network
from umqtt.simple import MQTTClient
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid_user,password)
time.sleep(5)
print(wlan.isconnected())

def connectMQTT():
    client = MQTTClient(client_id=b"stunr",
    server=b"jouw cluster url",
    port=8883,
    user=b"xxxxx",
    password=b"xxxxx",
    keepalive=7200,
    ssl=True,
    ssl_params={'server_hostname':'jouw cluster url'}
    )

    client.connect()
    return client

client = connectMQTT()

def publish(topic, value):
    print(topic)
    print(value)
    client.publish(topic, value)
    print("publish Done")
    
while True:
#Read sensor data ( de if moet je zelf aanpassen)
    if sensor.value()==0:
      
        publish('jouw topic', sensor.value)
    else:
        pass
#delay 5 seconds
    time.sleep(5)