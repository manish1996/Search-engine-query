import json

dic={}    #declare dict 
with open('postinglist.json') as f:  # .json file contains all the terms and respective list of docID
	dic = json.load(f)   # load file into dict 

with open('termfrequecy.json') as f:  # .json file contains all the terms and respective frequecies in all the doc's
	dic1 = json.load(f)   # load file into dict 

#for i in dic.keys():
#	print(i)
#	print(a[i])
term=input("enter the key you want to search")  # key whose docID want to know
if(term in dic):         # check if term exists in dict or not
	print("frequency of", term , "is" , dic1[term]) 
	print(dic[term])
else:
	print("not found")

print(len(dic[term]))