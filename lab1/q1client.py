import socket, string, os

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
	try:
		send_msg = str(raw_input("Message : "))
		s.send(send_msg)
		string = s.recv(1024)
		print string
	except KeyboardInterrupt:
		break
s.close()