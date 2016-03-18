import os
import time
import string
r1, w1 = os.pipe()
r4, w4 = os.pipe()
pid1 = os.fork()
if(pid1):
	os.close(r1)
	w1 = os.fdopen(w1, 'w')
	print "P1 PROCESS SENDING DATA"
	w1.write("hi")
	w1.close()
	os.close(w4)
	r4 = os.fdopen(r4)
	print "received from p2 :"+r4.read()
else:
	os.close(w1)
	r2, w2 = os.pipe()
	r3, w3 = os.pipe()
	pid2 = os.fork()
	if(pid2):
		r1 = os.fdopen(r1)
		print "receiving data from p1"
		msg = r1.read()
		print "data received from p1 through pipe:"+msg
		r1.close()
		os.close(r2)
		w2 = os.fdopen(w2, 'w')
		print "p2 forwarding data to p3"
		w2.write(msg)
		w2.close()
		os.close(w3)
		r3 = os.fdopen(r3)
		msg = r3.read()
		print "reply from p3:"+msg
		r3.close()
		os.close(r4)
		w4 = os.fdopen(w4, 'w')
		w4.write(msg[::-1])
		w4.close()
	else:
		os.close(w2)
		r2 = os.fdopen(r2)
		msg = r2.read()
		print "data received from p2 through pipe:"+msg
		r2.close()
		os.close(r3)
		w3 = os.fdopen(w3, 'w')
		print "reply sent to p2"
		w3.write(string.upper(msg))
		w3.close()
