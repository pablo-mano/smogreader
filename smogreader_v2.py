#!/usr/bin/python
import serial
import struct
import datetime
import time
import requests

# connect to SDL607 on Serial USB
ser = serial.Serial('/dev/ttyUSB0', 9600)

#confirm connection to device
print('connected to: ' + ser.portstr + ' at ' + str(datetime.datetime.now()))

#read and send data to file, dweet.io and opensmog API
while True:
 	output =  struct.unpack('BBBBBBBBBBBBBBBBBBB',ser.read(19))
	timestamp = datetime.datetime.now()
        n = datetime.datetime.now()
        unixtimestamp = time.mktime(n.timetuple())

	pm25 = output[8]*256 + output[7]
	pm10 = output[12]*256 + output[11]

	filecontent = str(timestamp) + ';' + str(pm25) + ';' + str(pm10) + '\n'
        dweetcontent = 'pm25=' + str(pm25) + '&pm10=' + str(pm10)
        opensmogjson = '[{ "timestamp": ' + str(int(unixtimestamp)) + ',"readings": {"PM2_5": ' + str(pm25*0.1) +',"PM10": ' + str(pm10*0.1) +'}}]'
	
	f = open('smogreader.txt','a')
	f.write(filecontent)
	f.close() 
	r = requests.get('https://dweet.io/dweet/for/12bf752c-b8a9-45c0-9ba4-a1d31165e948?'+dweetcontent)
	s = requests.post('http://httpbin.org/post', json=opensmogjson)
	
# OUTPUTS for debug
#       print(filecontent)
#       print(dweetcontent)
#       print(opensmogjson)                                                         
                                                         
