import socket, string, os

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

while True:
	try:
		s.listen(5)
		c, addr = s.accept()
		child_pid = os.fork()
		if child_pid == 0:
			print "Connected to : ", addr
			recv_msg = c.recv(1024)
			c.send(''.join(reversed(recv_msg)))
		else:
			pass
	except KeyboardInterrupt:
		break
c.close()
s.close()