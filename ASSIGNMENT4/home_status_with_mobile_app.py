import wiotp.sdk.device
import time
import random

myConfig = { 
    "identity": {
        "orgId": "d7luey",
        "typeId": "HomeStatus",
        "deviceId":"5683"
    },
    "auth": {
        "token": "12345678"
    }
}

lightsts = "OFF"
fansts = "OFF"
msgs = "HY"

def myCommandCallback(cmd):
    global lightsts  
    global fansts
    global msgs
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(m=="lighton"):
        lightsts = "ON"
    elif(m=="lightoff"):
        lightsts = "OFF"
    elif(m=="fanon"):
        fansts = "ON"
    elif(m=="fanoff"):
        fansts = "OFF"
    else:
        msgs = cmd.data['command']


        

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    roomTemp=random.randint(-10,60)
    humidity=random.randint(0,100)
    myData={'temperature':roomTemp, 'humidity':humidity,'light':lightsts,'fan':fansts,'mess':msgs}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
    
client.disconnect()
