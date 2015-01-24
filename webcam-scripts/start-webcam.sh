#! /bin/bash

cd /home/vandy/mjpg-streamer
./mjpg_streamer -i "./input_uvc.so -n -f 15 -r 1080x700 -l off" -o "./output_http.so -n -p 8088 -w ./var/www/mqtt-beaglebone/public_html"
