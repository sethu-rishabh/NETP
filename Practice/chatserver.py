#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import os
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
while True:
	child_pid = os.fork();
	if child_pid == 0:
	   	recv_msg = c.recv(1024)
	   	print recv_msg
	   	if recv_msg == "end":
	   		break
	else:
		message = str(raw_input())
	   	c.send(message)
	#if message == "end":
	#	break
c.close
s.close