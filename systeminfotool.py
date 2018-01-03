import sys
import socket

host = raw_input("What is the host IP?")

hostname = socket.getfqdn(host)

print "The hostname is:", hostname


