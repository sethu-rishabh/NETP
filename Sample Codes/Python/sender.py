import os

path = "/tmp/my_program.fifo"
os.mkfifo(path)

str1 = ""
while(str1 != "end"):
	fifo = open(path, "w")
	str1 = str(raw_input("Enter : "))
	fifo.write(str1)
	fifo.close()