import socket, sys, signal, os

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	try:
		s.sendto(str(raw_input()), (host,port))
		string = s.recv(1024)
		print string
	except KeyboardInterrupt:
		break
s.close()