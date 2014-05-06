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
import os
import subprocess


d= os.chdir('C:\\Users\\angell\\Documents\\Rails\\RasPiServer\\')
p = subprocess.Popen(["thin", "start"], shell=True)

def readTemp(roomNo):

	#Read the desired temp of a room
	data = {}

	roomNo = 'room' + str(roomNo) #need to add number to end of this string

	data['data'] = roomNo #e.g. 'room1'
	urlValues = urllib.urlencode(data)

	url = "http://localhost:3000/getTemp.json"

	full_url = url + '?' + urlValues
	print(full_url)

	#you can read back the temp with the line below
	data = urllib2.urlopen(full_url) #data will equal temp set on showRooms page

	print(data.read())

def logTemps(roomNo, reading):
	url = 'http://localhost:3000/logTemp.json'

	#the array below reads [room, temp reading]
	values = { 'data[]': [roomNo, reading] }
	data = urllib.urlencode(values, True)
	print data

	req = urllib2.Request(url,data)
	response = urllib2.urlopen(req)
	the_page = response.read() #reads server response e.g. status 200

	print 'logTemp ' + str(roomNo) +' ' + the_page

print(readTemp(2))
