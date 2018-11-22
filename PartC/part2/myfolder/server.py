import socket



def update(data):
	return data+"inside update"



sck= socket.socket()
print("created socket")

port=1234
var=1
sck.bind(("192.0.1.1",port))
#print("bind socke %s" (%port))
sck.listen(3)

print("socket is in listening mode")
shared_var=100
while True:
	shared_var+=100
	client,address=sck.accept()
	print("address", address)
	data=client.recv(1000)
	print("data", data+str(shared_var))
	recv= update(data+str(shared_var))
	client.send(recv)
	client.close
