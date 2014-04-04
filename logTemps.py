import urllib
import urllib2
import time

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

  

    
