import ephem
import math
import datetime
# import config file
import sys
sys.path.append('../')
import config

current_time = str(datetime.datetime.now())

location = ephem.Observer()
location.lon = config.siteLon
location.lat = config.siteLat
location.elevation = config.siteAlt
location.pressure = 0
location.date = current_time

line=[]

f = open("/tmp/stations.txt", "r")
searchlines = f.readlines()
f.close()
for i, line in enumerate(searchlines):
    if "ISS" in line:
        for l in searchlines[i:i+3]: line.append(str(l))
        #     exec("l%d = %s" % (i, l),
        # print("l%d" % (i)),
        # print

# print("l1: %s" % (l[0]))
# time.strftime("%Y/%m/%d %H:%M:%S")

# Load Satellite TLE data.
# l1 = 'ISS (ZARYA)'
# l2 = '1 25544U 98067A   15362.57617266  .00007229  00000-0  11208-3 0  9992'
# l3 = '2 25544  51.6430 193.9420 0008214 334.7441 131.3770 15.55152352978280'
# sat = ephem.readtle(l1,l2,l3)
# sat.compute(location)


# body = ephem.Mars(location)
# output Alt;AZ
# print("%s;%s" % (body.alt / ephem.degree, body.az / ephem.degree))
# print("AZ: %s" % (body.az / ephem.degree))

# print("Sat")
# print("AZ Deg: %s" % (sat.az / ephem.degree))
# print("ALT Deg: %s" % (sat.alt / ephem.degree))
# print("")
