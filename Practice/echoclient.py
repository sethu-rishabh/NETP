#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))

while True:
	send_msg = str(raw_input("Message : "))
	s.send(send_msg)
	if send_msg == "end" or send_msg == "bye":
		s.close
		break
	message = s.recv(1024)	#str(raw_input())
	#s.send(message + "\n")
	#if message == "end":
	#	s.close 
	#	break
	print message
                    # Close the socket when done