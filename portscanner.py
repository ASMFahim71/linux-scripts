#!/bin/python3
import sys
import socket
from datetime import datetime
#define target

if len(sys.argv) == 2:
	target=socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid amount of argument")
	print("Syntax: python 3 scanner.py <ip>")
	
#add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)


try:
	for port in range(1,1000):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))  #return an error indicator
		#print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is Open!".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()
except socket.gaierror: 
	print("Hostname could not br resolved.")
	sys.exit()
except socket.error:
	print("Could'nt Connect to server!")
	sys.exit()
