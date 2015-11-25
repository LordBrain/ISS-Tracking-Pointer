# Most of the code here is taken from Adafruit motor hat examples. Good job guys, you rock!

import sys
import time
import math
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import RPi.GPIO as GPIO
import pigpio


# Really start tracking stuff here. For real

# Read site location information.
import config
import objectList

#Servo stuff
servos = 25 #GPIO number
pi1 = pigpio.pi()
#pulsewidth can only set between 500-2500
pi1.set_servo_pulsewidth(servos, 0)

trackObject = int(sys.argv[1])
GPIO.setmode(GPIO.BCM)

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def findZero():
    #This is where I will find a known point on the steppers. Most likely using a analog line sensor
    while  True:
        # Servo Motion
        pi1.set_servo_pulsewidth(servos, 1000) #0 degree
        print("Servo {} {} micro pulses".format(servos, 1000))
        time.sleep(5)
        pi1.set_servo_pulsewidth(servos, 1500) #90 degree
        print("Servo {} {} micro pulses".format(servos, 1500))
        time.sleep(5)
        pi1.set_servo_pulsewidth(servos, 2000) #180 degree
        print("Servo {} {} micro pulses".format(servos, 2000))
        time.sleep(5)
        pi1.set_servo_pulsewidth(servos, 1500)
        print("Servo {} {} micro pulses".format(servos, 1500))
        time.sleep(5)
        pi1.set_servo_pulsewidth(servos, 1000) #0 degree
        print("Servo {} {} micro pulses".format(servos, 1000))
        # Move the stepper one step
        stepperX.step(1, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
        stepperY.step(1, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
        # Check for the line
        # Line finding Code!!!!!!

atexit.register(turnOffMotors)

stepperX = mh.getStepper(200, 1)       # 200 steps/rev, motor port #1 This is for the X Axis motor
stepperX.setSpeed(30)                  # 30 RPM

#
# # Move motors to zero
# findZero()

# command to get data from astro.
command = "/home/pi/Astro/libnova-0.15.0/examples/pointer_" + str(objectList.spaceObjects[trackObject]).lower()

# Debug testting stuff:
while True:
    print("Tracking:")
    print(trackObject)
    print(objectList.spaceObjects[trackObject])
    if not (trackObject == 0 or trackObject == 1):
        print("Tracking a Planet")
        process = Popen([command, "config.siteLat", "config.siteLon"], stdout=PIPE)
        (output, err) = process.communicate()
        print(output)
        planet=output.split()
        ra=planet[2]
        racalc=ra.split(':')
        rasec=float(racalc[2])
        calcrasec=rasec / 60
        ramin=float(racalc[1])
        calcramin=ramin / 60
        rahour=float(racalc[0])
        calcramin=ramin /60
        ratotal=rahour + calcramin + calcrasec
        radeg=ratotal * 15
        print("RA Deg: ")
        print(radeg)
        dec=planet[4]
        deccalc=dec.split(':')
        decsec=float(deccalc[2])
        calcdecsec=decsec / 60
        decmin=float(deccalc[1])
        calcdecmin=decmin / 60
        dechour=float(deccalc[0])
        dectotal=dechour + calcdecmin + calcdecsec
        print("Dec Deg: ")
        print(dectotal)

        exit_code = process.wait()
    else:
        print("Tracking satalite")
    time.sleep(5)
