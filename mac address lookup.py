import json
import urllib2
import codecs

mac = raw_input('What is the MAC address? ')
api = "http://macvendors.co/api/" + mac
info = urllib2.Request(api,headers={'User-Agent' : "API Browser"})
url = urllib2.urlopen(info)
reader = codecs.getreader("utf-8")
obj = json.load(reader(url))

print (obj['result']['company'])
print (obj['result']['address'])
