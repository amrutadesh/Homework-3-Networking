import socket
from threading import Thread
import time
import sys
import json
import ast
class Server(Thread):

	def __init__(self, ip, port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		print("inside server constructor")
	def run(self):
		s = socket.socket()
		s.bind((self.ip, self.port))
		s.listen(5)
		while True:
			print("ip server", self.ip)
			#            count= count + 1
			# checkUpdate(count)
			#            print("inside server ",count)
			c, addr = s.accept()
			
			
			data = c.recv(100)
			data=data.decode()
			updateWeights(data)
			print(data)
			#writef = open("out" + self.ip + ".txt", "a+")
			#writef.write(data)
			#writef.close()
			c.close()
def updateWeights(data):
	update=False
	print("inside update weights")
	recieved_data_from=str(data[2:4])
	datapoints =  eval(data)
	dataR=datapoints[recieved_data_from]
	print(dataR)
	# read sender'scurrent distance from me
	u=node_wt_dict[recieved_data_from]
	for v in node_wt_dict:
		if node_wt_dict[v] > u + dataR[v]:
			node_wt_dict[v]=u + dataR[v]
			update=True
	if(update):
		f=open(out_file,"a")
		f.write(str(node_wt_dict))
		f.write("\n")
		te=time.time()
		f.write(str(ts))
		f.write(str(te))
		f.write("\n")
		f.close()
		sendToClients()
				
def sendToClients():
	with open("nb.txt") as f:
		for line in f:
			info=line.split()
			if(info[0]==MY_IDT):
				
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				print("connecting to client :",info[1])
				client.connect((info[1], int(info[2])))
				sendData={}
				sendData[MY_IDT]=node_wt_dict
				
# 				r = json.dumps(sendData)
# 				loaded_r = json.loads(r)
				byt=str(sendData).encode()
				client.send(byt)
				#client.send(MY_IDT)
				client.close()

server=''
port=0
MY_IDT=''
out_file=''
node_wt_dict={'R1':10000,'R2':10000,'R3':10000,'R4':10000,'H1':10000,'H2':10000}
with open("node_info.txt") as f:
	for line in f:
		info=line.split()
		MY_IDT=sys.argv[1]
		if(info[0]==MY_IDT):
			server=info[1]
			port= int(info[2])
			
newThread = Server(server, port)
newThread.start()
time.sleep(60)


print("success")
i = 0
nb_dist=MY_IDT+"_nb.txt"
out_file=MY_IDT+"_out.txt"
node_wt_dict[MY_IDT]=0
with open(nb_dist) as m:
	for line in m:
		info=line.split()
		node_wt_dict[info[0]]=int(info[1])

print(node_wt_dict)
ts=time.time()
sendToClients()

# while (i < 10):
# # 	client = socket.socket()
# # 	client.connect(('localhost', 4444))
# # 	client.send(b'("Hello" + str(i))')
# # 	i += 1
# 	sendToClients()

