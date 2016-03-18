import socket
import datetime
import signal
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12347
s.bind((host, port))


while True:
	try :
		s.listen(5)
		c, addr = s.accept()
		print "Connected to : ", addr

		msg = str(datetime.datetime.now().time()) + "\n" + str(datetime.datetime.now().date())
		c.send(msg)
		c.close
	except KeyboardInterrupt:
		break
s.close