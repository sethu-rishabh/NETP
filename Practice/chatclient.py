#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import os
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                # Reserve a port for your service.

s.connect((host, port))

while True:
	child_pid = os.fork();
	if child_pid == 0 :
		send_msg = str(raw_input())
		s.send(send_msg)
		if send_msg == "end":
			s.close
			break
	else:		
		message = s.recv(1024)	#str(raw_input())
		#s.send(message + "\n")
		#if message == "end":
		#	s.close 
		#	break
		print message
                    # Close the socket when done