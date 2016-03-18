#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import os
import sys, signal

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

while True:
	try:
		s.listen(5)                 # Now wait for client connection.
		c, addr = s.accept()     # Establish connection with client.
		child_pid = os.fork()
		if child_pid == 0:
			print 'Got connection from', addr
			while True:
			   	recv_msg = c.recv(1024)
			   	#print recv_msg
			   	if recv_msg == "end" or recv_msg == "bye":
			   		print 'Terminated connection with', addr
			   		break
				#message = str(raw_input("Message : "))
			   	c.send(recv_msg)
				#if message == "end":
				#	break
		else :
			pass
	except KeyboardInterrupt:
		break
c.close
s.close