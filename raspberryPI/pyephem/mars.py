import ephem
import math
import datetime
# import config file
import sys
config.path.append('../')
import config

current_time = str(datetime.datetime.now())

location = ephem.Observer()
location.lon = siteLon
location.lat = siteLat
location.elevation = siteAlt
location.pressure = 0
location.date = current_time
# time.strftime("%Y/%m/%d %H:%M:%S")

# Load Satellite TLE data.
l1 = 'ISS (ZARYA)'
l2 = '1 25544U 98067A   15362.57617266  .00007229  00000-0  11208-3 0  9992'
l3 = '2 25544  51.6430 193.9420 0008214 334.7441 131.3770 15.55152352978280'
sat = ephem.readtle(l1,l2,l3)
sat.compute(location)


body = ephem.Mars(location)
print("Mars")
print("Alt: %s" % (body.alt / ephem.degree))
print("AZ: %s" % (body.az / ephem.degree))

print("Sat")
print("AZ Deg: %s" % (sat.az / ephem.degree))
print("ALT Deg: %s" % (sat.alt / ephem.degree))
print("")
