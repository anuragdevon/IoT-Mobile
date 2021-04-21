import json
import socket
import time
import sys
import base64

LIGHT = []
PROXIMITY = []
ACCELEROMETERX = []
ORIENTATIONX = []
ORIENTATIONY = []

def animate():
    i = 0
    while(i<2):
        sys.stdout.write("\rUploading Model-S's Data... |")
        time.sleep(0.3)
        sys.stdout.write("\rUploading Model-S's Data... /")
        time.sleep(0.3)
        sys.stdout.write("\rUploading Model-S's Data... -")
        time.sleep(0.3)
        sys.stdout.write("\rUploading Model-S's Data... \\")
        time.sleep(0.3)
        i+=1
def midLoad():
    i = 0
    while(i<2):
        sys.stdout.write("\r|")
        time.sleep(0.3)
        sys.stdout.write("\r/")
        time.sleep(0.3)
        sys.stdout.write("\r-")
        time.sleep(0.3)
        sys.stdout.write("\r\\")
        time.sleep(0.3)
        i+=1

animate()
time.sleep(0.1)
print("\n")

with open('model-s.json') as sensors:
    data = json.load(sensors)

for x in data:
    for i in x:
        if i == 'LIGHT':
            LIGHT.append(x[i])
        elif i == "PROXIMITY":
            PROXIMITY.append(x[i])
        elif i == "ACCELEROMETERX":
            ACCELEROMETERX.append(x[i])
        elif i == "ORIENTATIONX":
            ORIENTATIONX.append(x[i])
        elif i == "ORIENTATIONY":
            ORIENTATIONY.append(x[i])

# Application 1: Calculate the chances of Accident and Alert the driver or open Airbag
print("\nGenrating possible Accident related chances: ")
msgAccident=[]
for i in range(4):
    if int(PROXIMITY[i]) > 0 and float(ACCELEROMETERX[i]) > 8.0 :
        if(float(ACCELEROMETERX[i]) > 10.0):
            print("Airbag is about to burst in Model-S!")
            msgAccident.append("Airbag is about to burst in Model-S!")
        else:
            print("Alert! Model-S might encounter an accident.")
            msgAccident.append("Alert! Model-S might encounter an accident.")
    else:
        print("Model-S is running safe on road")
        msgAccident.append("Model-S is running safe on road")

midLoad()
# Application 2: Calculate whether we should start the headlight of the car 
print("\n\nSituation of Model-S's Headlights: ")
msgLight=[]
for i in range(4):      
    if(int(LIGHT[i]) < 400):
        print("ON")
    else:
        print("OFF")

midLoad()
# Application 3: Gear Control Mechanism
print("\n\nSome Gear shit:")
msgChangeGear=[]
for i in range(4):   
    if (float(ORIENTATIONY[i]) > 15 and float(ORIENTATIONY[i]) < 30):
        print("Switch to gear 2")
    else:
        print("Switch to gear 1")

midLoad()
# Application 4: Direction of the Car
print("\n\nDirection Model-S is Moving to:  ")
msgDirection=[]
for i in range(4):

    if(float(ORIENTATIONX[i]) >= 0 and float(ORIENTATIONX[i]) < 90):
        if(float(ORIENTATIONX[i]) == 0):
            print("North")
            msgDirection.append("North")
        else:
            print("North-East")
            msgDirection.append("North-East")

    elif(float(ORIENTATIONX[i]) >= 90 and float(ORIENTATIONX[i]) < 180):
        if(float(ORIENTATIONX[i]) == 90):
            print("East")
            msgDirection.append("East")
        else:
            print("South-East")
            msgDirection.append("South-East")

    elif(float(ORIENTATIONX[i]) >= 180 and float(ORIENTATIONX[i]) < 270):
        if(float(ORIENTATIONX[i]) == 180):
            print("South")
            msgDirection.append("South")
        else:
            print("South-West")
            msgDirection.append("South-West")

    elif(float(ORIENTATIONX[i]) >= 270 and float(ORIENTATIONX[i]) < 360):
        if(float(ORIENTATIONX[i]) == 270):
            print("West")
            msgDirection.append("West")
        else:
            print("North-West")
            msgDirection.append("North-West")

midLoad()
host = '192.168.43.248'
# host = '127.0.0.1'
PORT = 12348
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, PORT))

print("\nSending accident and direction data to server for further analysis...\n")
msg=[msgAccident, msgDirection]
msg=str(msg)
msg=msg.encode()
sock.send(msg)
midLoad()
print("\nMessage Sent Successfully!")
print("\nWaiting For Server to get results...\n")
print("\nResults have been shared!\n")

sock.close()
print("Waiting for remote cloud to analyze the system...")
midLoad()
time.sleep(20)
def Reciever():
    Req = requests.get('https://api.thingspeak.com/channels/1365930/feeds.json?api_key=J5I5AHEWEZSHGMXE&results=2')
    if Req.ok:
        Information = Req.json().get('feeds')
        return Information
    else:
        # unsucessfull termination
        exit(1)
print("\nCopy of Feedback got from remote cloud analysis...\n")