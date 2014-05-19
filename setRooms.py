#!/usr/bin/env python 


import os
import urllib
import urllib2
import time

import subprocess



os.chdir('/home/loubot/Desktop/piTester')
os.system('pwd')
x = subprocess.Popen('./startRails.py')


print x

checker= True
while checker:
        try:
                data = urllib2.urlopen('http://localhost:3000/checkOk')
                if data.read() == 'ok':
                        checker = False
                
        except :
                print 'Server not ready yet!'

##        print a
##        print d
        time.sleep(6)

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
	print(the_page)
	print 'logTemp ' + str(roomNo) +' ' + the_page

print(readTemp(2))
logTemps(1, 23)



