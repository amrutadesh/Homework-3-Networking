import sys
import socket 
import threading
import time

count=0
def server(ip):
        global count
        s = socket.socket()         
        print ("Socket successfully created")
        port = 4444               
         
        
        s.bind((ip,port))        
        print ("socket binded to %s" %(port))
         
        
        s.listen(5)     
        print (b"socket is listening")           
         
        
        while True:
            
            count= count+1
            #checkUpdate(count)
            print("inside server ",count)
            c, addr = s.accept()     
            print ('Got connection from', addr)
            print ("data", c.recv(100))
            
            c.close()
def client(ipToSend):
    count_tem=0
    i=0
    while (i<100):
    
        print("in while ", count)
        s = socket.socket()         
        print ("Socket successfully created")
         
        # reserve a port on your computer in our
        # case it is 12345 but it can be anything
        port = 12345               
         
        # Next bind to the port
        # we have not typed any ip in the ip field
        # instead we have inputted an empty string
        # this makes the server listen to requests 
        # coming from other computers on the network
        
        
        s.connect((ipToSend, 4444))
        s.send(b'Hello, world')
        
        s.close()
        i+=1
                
if __name__ == '__main__':
    t = threading.Thread(name='daemon', target=server(sys.argv[1]))
    t.start()
    time.sleep(30)
    client(sys.argv[2])   
    
    # def checkUpdate(count):
    #     print("inside check update")
    #     time.sleep(2)
    #     
    #     print(count)
    #     time.sleep(4)
    #     print(count)
    #     s = socket.socket()         
    #     print ("Socket successfully created")
    #      
    # 
    #     
    #     s.connect(("localhost", 4444))
    #     s.send(b'Hello, world check1')
    #     data = s.recv(1024)
    #     s.close()
    #     
    #     print(data)
    
    

# print("amruta")
# 
# s = socket.socket()         
# print ("Socket successfully created")
#  
# # reserve a port on your computer in our
# # case it is 12345 but it can be anything
# port = 4444               
#  
# # Next bind to the port
# # we have not typed any ip in the ip field
# # instead we have inputted an empty string
# # this makes the server listen to requests 
# # coming from other computers on the network
# 
# 
# s.connect(("localhost", 12345))
# s.send(b'Hello, world')
# data = s.recv(1024)
# s.close()
# print(data)
# s = socket.socket()         
# print ("Socket successfully created")
#  
# # reserve a port on your computer in our
# # case it is 12345 but it can be anything
# port = 4444               
#  
# # Next bind to the port
# # we have not typed any ip in the ip field
# # instead we have inputted an empty string
# # this makes the server listen to requests 
# # coming from other computers on the network
# 
# 
# s.connect(("localhost", 12345))
# s.send(b'Hello, world')
# data = s.recv(1024)
# s.close()
# print(data)
