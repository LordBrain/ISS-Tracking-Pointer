import sys
import location
import objectList
import config
from subprocess import Popen, PIPE

trackObject = int(sys.argv[1])

print location.siteLat
print("Tracking:")
print(trackObject)
print(objectList.spaceObjects[trackObject])

command = "/home/pi/Astro/libnova-0.15.0/examples/pointer_" + str(objectList.spaceObjects[trackObject]).lower()
print(command)
process = Popen([command, "config.siteLat", "config.siteLon"], stdout=PIPE)
(output, err) = process.communicate()
print(output)
exit_code = process.wait()
