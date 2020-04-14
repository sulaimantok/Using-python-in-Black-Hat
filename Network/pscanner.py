import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of argumnet.")
	print("Syntax: python3 scanner.py <ip>")

print("-"* 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-"* 50)

try:
	for port in range(1,500):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		#print("Checking port {}".format(port))
		if result == 0:
			print("port {} is open".format(port))
		s.close
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
