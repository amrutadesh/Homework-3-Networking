import socket 
import threading
import time
import sys

count=0
node_ip=""

def dataRecv(c):
	while True:
		data=c.recv(100)



def server(ip):
#        global count
        s = socket.socket()         
	print ("Socket successfully created")
        port = 4444               
         
        
        s.bind(('', port))        
#        print ("socket binded to %s" %(port))
         
        
        s.listen(5)     
        print (b"socket is listening")           
         
        
        while True:
            print("ip server",ip)
#            count= count + 1
            #checkUpdate(count)
#            print("inside server ",count)
            c, addr = s.accept()    
	        
	    writef=open("out"+ip+".txt","w+")
#	    data=c.recv(100)
	    
            writef.write(data)
            writef.close()
 
#        print ('Got connection from', addr)
            #print ("data", c.recv(100))
            c.close()

t = threading.Thread(name='daemon', target=server(sys.argv[2]))
t.setDaemon(True)
t.start()
     

count_tem=0
#def clientCall(host):
#	print("inside client ")
	
#if __name__ == "__main__":
#print("inside",sys.argv[1],sys.argv[2])
t = threading.Thread(name='non-daemon', target=server(sys.argv[2]))
#t.daemon = True
t.start()	   
time.sleep(3)
#	clientCall(sys.argv[1])
print("success",sys.argv[1])

s = socket.socket()         
print ("Socket successfully created")
port = 4444               
s.connect((output[1], 4444))
s.send(b'Hello, world')
#data = s.recv(1024)
writef=open("out.txt","w+")
writef.write("Amruta")
writef.close()
s.close()

#	while True:
#	    print("inside client while")

#	    if (1):
#		count_tem=count
#		print("inside client")
#		with open("/home/mininet/myfolder/client.txt") as f:
#			for line in f:
#				print("line",line)
#				output= line.split()
#				if(output[0] == host):
#					count_tem=count
#					print("in while ",output[1] )
#					s = socket.socket()         
#					print ("Socket successfully created")
					 
					# reserve a port on your computer in our
					# case it is 12345 but it can be anything
#					port = 4444               
					 
					# Next bind to the port
					# we have not typed any ip in the ip field
					# instead we have inputted an empty string
					# this makes the server listen to requests 
					# coming from other computers on the network
					
					
#					s.connect((output[1], 4444))
#					s.send(b'Hello, world')
#					#data = s.recv(1024)
#					writef=open("out.txt","w+")
#					writef.write("Amruta")
#					writef.close()
#					s.close()
					
					#print(data)


