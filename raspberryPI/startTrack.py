# Most of the code here is taken from Adafruit motor hat examples. Good job guys, you rock!

import sys
import time
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import RPi.GPIO as GPIO

# Really start tracking stuff here. For real

# Read site location information.
import config
import objectList

print("startTrack.py")
trackObject = int(sys.argv[1])
GPIO.setmode(GPIO.BCM)
X_LINE_PIN = 5 # Line Sensor Pin
Y_LINE_PIN = 6 # Line Sensor Pin

GPIO.setup(X_LINE_PIN, GPIO.IN)
GPIO.setup(Y_LINE_PIN, GPIO.IN)

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
        # Move the stepper one step
        stepperX.step(1, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
        stepperY.step(1, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
        # Check for the line
        # Line finding Code!!!!!!

atexit.register(turnOffMotors)

# stepperX = mh.getStepper(200, 1)       # 200 steps/rev, motor port #1 This is for the X Axis motor
# stepperX.setSpeed(30)                  # 30 RPM
#
# stepperY = mh.getStepper(400, 2)       # 400 steps/rev, motor port #1 This is for the Y Axis motor
# stepperY.setSpeed(30)                  # 30 RPM
#
# # Move motors to zero
# findZero()

# Debug testting stuff:
while True:
    print("Tracking:")
    print(trackObject)
    print(objectList.spaceObjects[trackObject])
    time.sleep(5)
