import urllib
import urllib2
import time

roomNo = 1
reading = 20

while True:

    url = 'http://localhost:3000/logTemp.json'

    #the array below reads [room, temp reading]
    values = { 'data[]': [roomNo, reading] }
    data = urllib.urlencode(values, True)
    print data

    req = urllib2.Request(url,data)
    response = urllib2.urlopen(req)
    the_page = response.read()

    print 'logTemp ' + the_page

    if roomNo >= 4:
        roomNo = 1
    else:
        roomNo += 1

    reading += 1

    time.sleep(5)
