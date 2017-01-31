# Smog Reader
## Hardware:
Device SDL607 Air Quality Monitor, which measures with laser Particulate Matter (PM2.5 & PM10)

![SDL607 Device picture](https://github.com/pawel-manu/smogreader/blob/master/SDL607_RPi_smogreader.jpg)

Device connected via USB to Raspberry PI

## Output: 
Data sent to Dweet.io - you can follow:

https://dweet.io/follow/12bf752c-b8a9-45c0-9ba4-a1d31165e948

or see dashboard:

https://freeboard.io/board/1SeVCD

Prepared to send data to OpenSmog / AcquisitionAPI 

https://github.com/OpenSmog/AcquisitionAPI

## Scripts: 

smogreader_v2.py - readings

smogreader_start.sh - script for crontab

Add to cron following line to run this script during reboot:

@reboot /home/pi/smogreader/smogreader_start.sh

Required lib: 

Requests http://docs.python-requests.org/

## Contact: 

Mail: manowiecki@gmail.com

Twitter: @pawel_manu
