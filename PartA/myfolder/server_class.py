import socket
from threading import Thread
import time

class Server(Thread):
	def __init__(self,ip,port):
		Thread.__init__(self)
		self.ip=ip
		self.port=port
		print("inside server constructor")
	def run(self):
		s = socket.socket()
		print ("Socket successfully created")
        	#port = 4444


        	s.bind((self.ip, self.port))
#        print ("socket binded to %s" %(port))


        	s.listen(5)
        	print (b"socket is listening")


        	while True:
           		 print("ip server",self.ip)
#            count= count + 1
            #checkUpdate(count)
#            print("inside server ",count)
            		 c, addr = s.accept()

            		 writef=open("out"+self.ip+".txt","a+")
	                 data=c.recv(100)

            		 writef.write(data)
            		 writef.close()
			 c.close()



newThread= Server('192.0.1.1',4444)
newThread.start()
time.sleep(10)
print("success")
i=0
while (i<10):
	client =socket.socket()
	client.connect(('192.0.1.1',4444))
	client.send("Hello"+str(i))
	i+=1


