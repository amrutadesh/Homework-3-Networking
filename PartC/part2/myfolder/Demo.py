import json
node_wt_dict={'R1':1000,'R2':1000,'R3':1000,'R4':1000,'H1':1000,'H2':1000}
data=str(node_wt_dict)

print(data)
#print( data['R1'])

# x = json.loads("{\"foo" : 'bar', "hello" : 'world'}")
# print(type(x))
# import pickle
# x=pickle.dumps(data)
# 
# print(pickle.loads(x))
dictNames = eval(data)
print(dictNames['R1'])