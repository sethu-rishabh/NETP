import os
import sys

path = "/tmp/my_program.fifo"
fifo = open(path, "r")
while True:
	line = fifo.read(1024)
	if(line != "end"):
		print "Received : " + line
	else:
		break
fifo.close()