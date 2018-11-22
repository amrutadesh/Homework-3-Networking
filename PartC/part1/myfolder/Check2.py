
import socket 
import threading
import time

count=0
def server():
        global count
        s = socket.socket()         
        print ("Socket successfully created")
        port = 12345               
         
        
        s.bind(( '',port))        
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

   
    
def client():
    count_tem=0  
    i=0 
    while (i<100):
       # if (count_tem!=count):
            count_tem=count
            print("in while ", count)
            s = socket.socket()         
            print ("Socket successfully created")
             
            # reserve a port on your computer in our
            # case it is 12345 but it can be anything
            port = 4444               
             
            # Next bind to the port
            # we have not typed any ip in the ip field
            # instead we have inputted an empty string
            # this makes the server listen to requests 
            # coming from other computers on the network
            
            
            s.connect(("localhost", 12345))
            s.send(b'Hello, world')
            
            s.close()
    	    i+=1
if __name__ == '__main__':    
    t = threading.Thread(name='non-daemon', target=server)
    t.start()    
    time.sleep(4)
    #y = threading.Thread(name='non-daemon', target=client)
    #y.start()   
    client()
            
            
            
        
        
    
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
