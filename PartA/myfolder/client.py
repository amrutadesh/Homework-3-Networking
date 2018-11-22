import socket
import shared
sck= socket.socket()
sck.connect(("192.0.1.1",1234))
sck.send(b"Hellow")
data=sck.recv(1000)
print(shared.shared_var)
sck.close()

print("recieved data",data)
