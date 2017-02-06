#!/usr/bin/python
import serial
import struct
import datetime
import time
import requests
from Adafruit_BME280 import *

# connect to SDL607 on Serial USB and BME280 on I2C
ser = serial.Serial('/dev/ttyUSB0', 9600)
sensor = BME280(mode=BME280_OSAMPLE_8)


#confirm connection to device
print('connected to: ' + ser.portstr + ' at ' + str(datetime.datetime.now()))

#read and send data to file, dweet.io and opensmog API
while True:

        # read output of SDL607
 	output =  struct.unpack('BBBBBBBBBBBBBBBBBBB',ser.read(19))

        #parse output to particle matter measures
	pm25 = (output[8]*256 + output[7])/10.0
	pm10 = (output[12]*256 + output[11])/10.0

    # read output of BME280
    temperature = round(sensor.read_temperature(),2)
    pressure_pascals = round(sensor.read_pressure(),2)
    pressure = round(pressure_pascals / 100,2)
    humidity = round(sensor.read_humidity(),2)

    # get timestamps
    timestamp = datetime.datetime.now()
    n = datetime.datetime.now()
    unixtimestamp = time.mktime(n.timetuple())

    #build content for file, dweet.io, opensmog.api
	filecontent = str(timestamp) + ';' + str(pm25) + ';' + str(pm10) + ';' + str(temperature) + ';' + str(pressure) + ';' + str(humidity) + '\n'
    dweetcontent = 'timestamp=' + str(int(unixtimestamp)) + '&pm25=' + str(pm25) + '&pm10=' + str(pm10)+ '&temp=' + str(temperature)+ '&press=' + str(pressure) + '&hum=' + str(humidity)
    opensmogjson = [{ "timestamp" : int(unixtimestamp) , "readings" : {"pm2_5": pm25 , "pm10" : pm10 , "temp": temperature , "hum" : humidity , "press":  pressure }}]
	
	f = open('smogreader_sdl_bme.txt','a')
	f.write(filecontent)
	f.close() 
	r = requests.get('http://dweet.io/dweet/for/{SUID}?key={KEY}&'+dweetcontent)
	s = requests.post('http://{SMOGAPI_ENDPOINT}/sensors/{SUID}/readings', json=opensmogjson)
	
# OUTPUTS for debug
#        print(filecontent)
#        print(dweetcontent)
#        print(opensmogjson)
#		 print(s)
#		 print(s.text)
