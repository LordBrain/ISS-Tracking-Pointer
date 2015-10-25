import sys
import math
import time
from main import spaceObjects

#This will be where the tracking happens.
#load location information
execfile('location.py')

# Object list
execfile('objectList.py')

#arguments passed from main.
trackObject = int(sys.argv[1])

#debug info
print("Tracking:")
print(trackObject)
print("Site Lat Rad:")
print(siteLatRad)
print("Site Long Rad:")
print(siteLonRad)
print(spaceObjects[0])
