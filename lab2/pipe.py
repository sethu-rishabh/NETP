import os,sys

print "Child process sending data"
print "Parent process receiving data"

r1, w1 = os.pipe() 
r2, w2 = os.pipe()
pid = os.fork()

if pid:
	pid = os.getpid()
	os.close(w1)
	os.close(r2)
	r1 = os.fdopen(r1, 'r')
	w2 = os.fdopen(w2, 'w')
	recv_msg = r1.read()
	r1.close()
	print "[", pid, "] Data received from child through pipe : ", recv_msg
	print "[", pid, "] Reply send"
	send2 = str(raw_input("Enter : "))
	w2.write(send2)
	w2.close()
	sys.exit(0)
else:
	pid = os.getpid()  
	os.close(r1)
	os.close(w2)
	w1 = os.fdopen(w1, 'w')
	r2 = os.fdopen(r2, 'r')
	send_msg = str(raw_input("Enter : "))
	w1.write(send_msg)
	w1.close()
	recv2 = r2.read()
	print "[", pid, "] Reply from parent : ", recv2
	r2.close()
	sys.exit(0)