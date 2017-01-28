#!/usr/bin/python
from time import sleep
import serial
import struct
import datetime
import requests

# Establish the connection on a specific port
ser = serial.Serial('/dev/ttyUSB0', 9600) 

print("connected to: " + ser.portstr + " at " + str(datetime.datetime.now()))
 
while True:
 #      print binascii.b2a_base64(ser.read(19)) # Read the newest output 
	output =  struct.unpack("BBBBBBBBBBBBBBBBBBB",ser.read(19))
	stempelczasu = datetime.datetime.now()
	pm25 = output[8]*256 + output[7]
	pm10 = output[12]*256 + output[11]
	f = open('smogreader.txt','a')
	f.write(str(stempelczasu) + ';' + str(pm25) + ';' + str(pm10) + '\n')
#	print(str(stempelczasu) + '|' + str(pm25) + '|' + str(pm10))
	f.close() 
	r = requests.get("https://dweet.io/dweet/for/12bf752c-b8a9-45c0-9ba4-a1d31165e948?pm25=" + str(pm25) + "&pm10=" + str(pm10))	
