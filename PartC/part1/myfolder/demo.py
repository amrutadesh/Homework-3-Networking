import threading
import time
import socket


class mythread(threading.Thread):
	h=0
	def __int__(self,i):
		threading.Thread.__init__(self)
		self.h=i
	def run(self):
		time.sleep(0.5)
		#while (True):
		print("value send",self.h)
		s=socket.socket()
		s.bind((str(self.h),4444))
		s.listen(5)
		c,addr= s.accept()
		print(c.recv(100))
		c.close()
		

#for i in range(10):
thread1=mythread(args='192.0.1.1')
thread1.start()


print("active threads are",threading.activeCount())
