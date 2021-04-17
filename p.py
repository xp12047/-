import os
path=os.path.split(os.path.realpath(__file__))[0]

a=123
with open(os.path.join(path,'test.txt'),mode='w',encoding='utf8') as f:
	f.write(str(a))
	#print('suc')

with open(os.path.join(path,'test.txt'),mode='r',encoding='utf8') as f:
	result=f.readlines()[0]
	print(result)




