"""
Develop a code to upload the water tank level and light intensity values
to the IBM IoT platform and visualize them in the web application.

"""


import wiotp.sdk.device
import time
import random

myConfig = { 
    "identity": {
        "orgId": "d7luey",
        "typeId": "WaterAndLight",
        "deviceId":"5682"
    },
    "auth": {
        "token": "12345678"
    }
}

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    waterLevel=random.randint(0,100)
    lightIntensity=random.randint(0,100)
    myData={'level':waterLevel, 'intensity':lightIntensity}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    time.sleep(2)
    
client.disconnect()
