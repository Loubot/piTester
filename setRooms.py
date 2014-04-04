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

def readTemp(roomNo):

	#Read the desired temp of a room
	data = {}

	data['data'] = roomNo #'room1'
	urlValues = urllib.urlencode(data)

	url = "http://localhost:3000/getTemp.json"

	full_url = url + '?' + urlValues
	print(full_url)

	#you can read back the temp with the line below
	data = urllib2.urlopen(full_url) #data will equal temp set on showRooms page

	print(data.read())
