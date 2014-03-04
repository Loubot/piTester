#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      angell
#
# Created:     03/03/2014
# Copyright:   (c) angell 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2
import urllib

#Set the desired temperature. 
url = "http://localhost:3000/setTemp.json"
#The array below reads [room, reading]
values = {'data[]': [1, 100]}

data = urllib.urlencode(values, True)
print(data)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

print "setTemp " + the_page


#Read the desired temp of a room
data = {}

data['data'] = 'room1'
urlValues = urllib.urlencode(data)

url = "http://localhost:3000/getTemp.json"

full_url = url + '?' + urlValues
print(full_url)
#you can read back the temp with the line below
data = urllib2.urlopen(full_url)

print(data.read())
