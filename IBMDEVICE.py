import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
organization = "z2iz6p"
deviceType = "raspberrypi"
deviceId = "123456"
authMethod = "token"
authToken = "12345678"


def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        print(type(cmd.data))
        i=cmd.data('command')
        if i=='motoron':
               print("motor is on")
        elif i=='motoroff':
            print("motor is off")
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        
        hum=random.randint(40, 90)
        temp =random.randint(30, 45)
        data = { 'Temperature' : temp, 'Moisture': hum }

        if hum<=50:
                r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=FPYnw1x9CrHcIk6R3AqTpOeZzvi85lQyjLa4dDJgMGVmf02suKFjdvKuCfeWxa8oY59y6Xw1b3R7UlJH&sender_id=FSTSMS&message=turnmotoron&language=english&route=p&number=9154023236')
                print(r.status_code)
        
        def myOnPublishCallback():
            print ("Published Temperature = %s C" % temp, "Moisture = %s %%" % hum, "to IBM Watson")

        success = deviceCli.publishEvent("DHT11", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback

deviceCli.disconnect()
