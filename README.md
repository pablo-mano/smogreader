# Smog Reader
## Hardware:
Device SDL607 Air Quality Monitor, which measures with laser Particulate Matter (PM2.5 & PM10)

Device manual: http://inovafitness.com/software/SDL607%20Laser%20PM2.5%20Monitor%20V1.2.pdf

Version RPi + SDL607 (v2): 

![SDL607 Device picture](https://github.com/pawel-manu/smogreader/blob/master/SDL607_RPi_smogreader_v2.jpg)

Version RPi + SDL607 + BME280 (v3):

![SDL607 Device with BME sensor picture](https://github.com/pawel-manu/smogreader/blob/master/SDL607_RPi_smogreader_v3.jpg)

SDL607 connected via USB to Raspberry PI

BME280 connected to Raspberry PI via I2C pins

## Output: 
Data sent to Dweet.io, what you see live on this dashboard:

https://freeboard.io/board/1SeVCD

Prepared to send data to OpenSmog / AcquisitionAPI 

https://github.com/OpenSmog/AcquisitionAPI

## Scripts: 

smogreader_v2.py - readings RPi + SDL607

smogreader_v3.py - readings RPi + SDL607 + BME280

smogreader_start.sh - script for crontab (for v3)

Add to cron following line to run this script during reboot:

```@reboot /home/pi/smogreader/smogreader_start.sh```

Required lib: 

Requests http://docs.python-requests.org/
Adafruit BME https://github.com/adafruit/Adafruit_BME280_Library

## Contact: 

Mail: manowiecki@gmail.com

Twitter: @pawel_manu
