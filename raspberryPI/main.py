#Main menu for raspberry pi ISS & others tracker

#Uses the OLED display monochrome display from Adafruit.
#Code adapted from The Raspberry Pi Guy's examples.

import gaugette.ssd1306
import time
import sys
import math
import subprocess
import RPi.GPIO as GPIO
import urllib


def displayMenuOption( menuID, selected ):
    #Update Display with new menu name
    led.clear_display()
    text = spaceObjects[menuID]
    led.draw_text2(0,0,text,3)
    if(menuID == selected):
        led.draw_text2(0,22,"Tracking",1)
    led.display()
    return

#start tracking on button push
def trackThing( trackID ):
    #First kill any existing tracking script
    #Start new tracking script
    subprocess.call(['python', 'track.py',str(trackID)])
    return


# Setting some variables for our pins
RESET_PIN = 15 #Display Reset
DC_PIN    = 16 #Display Power
LEFT_BUTTON_PIN = 21 #Button
RIGHT_BUTTON_PIN = 20 #Button
SELECT_BUTTON_PIN = 26 #Button

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT_BUTTON_PIN, GPIO.IN)
GPIO.setup(RIGHT_BUTTON_PIN, GPIO.IN)
GPIO.setup(SELECT_BUTTON_PIN, GPIO.IN)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display() # This clears the display but only when there is a led.display() as well!

#CODE HERE TO DOWNLOAD ORBIT FILES
#Space Station
text = "Downloading"
text2 = "Space Station"
text3 = "Orbit"
led.clear_display()
led.draw_text2(0,0,text,1)
led.draw_text2(0,10,text2,1)
led.draw_text2(0,20,text3,1)
led.display()
time.sleep(2)
try:
    urllib.urlretrieve("http://www.celestrak.com/NORAD/elements/stations.txt","stations.txt")
except Exception as e:
    text = "Error downloading"
    text2 = "Space Station"
    text3 = "Orbit"
    text4 = str(e)
    led.clear_display()
    led.draw_text2(0,0,text,1)
    led.draw_text2(0,10,text2,1)
    led.draw_text2(0,20,text4,1)
    #led.draw_text2(0,30,text4,1)
    led.display()
    time.sleep(2)


#Hubble (HST), other science based ones.
text = "Downloading"
text2 = "Science Based"
text3 = "Satalittes"
led.clear_display()
led.draw_text2(0,0,text,1)
led.draw_text2(0,15,text2,1)
led.draw_text2(0,30,text3,1)
led.display()
time.sleep(2)
try:
    urllib.urlretrieve("http://www.celestrak.com/NORAD/elements/science.txt","science.txt")
except Exception as e:
    text = "Error downloading"
    text2 = "Science Based"
    text3 = "Satalittes"
    text4 = str(e)
    led.clear_display()
    led.draw_text2(0,0,text,1)
    led.draw_text2(0,15,text2,1)
    led.draw_text2(0,30,text3,1)
    led.draw_text2(0,45,text4,1)
    led.display()
    time.sleep(2)

#Objects to track, IN SPACE!!!
execfile('objectList.py')
#defaults to tracking the ISS
trackingSelected = 0
tracking = 0
#first run on startup
displayMenuOption(tracking,trackingSelected)
trackThing(trackingSelected)

while True:
    if(GPIO.input(LEFT_BUTTON_PIN) == False):
        print("left button pushed")
        tracking -= 1
        if( tracking < 0 ):
            tracking = len(spaceObjects) - 1
        #Update display function
        displayMenuOption(tracking,trackingSelected)
        time.sleep(.5)
    elif(GPIO.input(SELECT_BUTTON_PIN) == False):
        print("select button pushed")
        trackingSelected = tracking
        displayMenuOption(tracking,trackingSelected)
        trackThing(trackingSelected)
        time.sleep(.5)
    elif(GPIO.input(RIGHT_BUTTON_PIN) == False):
        print("right button pushed")
        tracking += 1
        if( len(spaceObjects) - 1 < tracking ):
            tracking = 0
        #Update display function
        displayMenuOption(tracking,trackingSelected)
        time.sleep(.5)
        #
