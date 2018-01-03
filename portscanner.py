import socket
import subprocess
import sys


remoteServer = raw_input("Enter a host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(.25)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}:         Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Force quit"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldnt connect to server"


print 'Scanning Completed'

