#!/bin/bash
STATE="error";

while [  $STATE == "error" ]; do
    #do a ping and check that its not a default message or change to grep for something else
    STATE=$(ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error)

    #sleep for 2 seconds and try again
    sleep 2
 done

cd /home/pi/smogreader
python smogreader_v2.py >> smogreader_v2.log 2>&1
