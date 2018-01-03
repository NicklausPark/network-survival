import sys
import socket

hostname = raw_input('What is the hostname?')
ip = socket.gethostbyname(hostname)

print "The IP address of target is:", ip