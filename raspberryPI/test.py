import sys
import location
import objectList
from subprocess import Popen, PIPE

trackObject = int(sys.argv[1])

print location.siteLat
print("Tracking:")
print(trackObject)
print(objectList.spaceObjects[trackObject])


process = Popen(["ls", "-la", "."], stdout=PIPE)
(output, err) = process.communicate()
print(output)
exit_code = process.wait()
