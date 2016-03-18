import socket, sys, signal, os, string

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))


while True:
	try:
		(string, addr) = s.recvfrom(1024)
		pid = os.fork()
		if(pid ==  0):
			s.sendto(string.upper(), addr)
			break
		else:
			pass
	except KeyboardInterrupt:
		break
s.close()