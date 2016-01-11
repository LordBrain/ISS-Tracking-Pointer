#!/usr/bin/python

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

space_array = []

f = open("/tmp/stations.txt", "r")
searchlines = f.readlines()
f.close()
for i, line in enumerate(searchlines):
    if "ISS" in line:
        for l in searchlines[i:i+3]: space_array.append(l)

sat = ephem.readtle(space_array[0],space_array[1],space_array[2])
sat.compute(location)
# output Alt;AZ
print("%s;%s" % (sat.alt / ephem.degree, sat.az / ephem.degree))
