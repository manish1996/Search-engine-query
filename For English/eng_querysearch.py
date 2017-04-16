import json
import os
import tfidf_eng
import fnmatch
import pickle
import math
import re
from tfidf_eng import IRIndexing
import string
class Tfqu():
	def __init__(self):
		dic={}             		# to laod pickle inverted index file					
		f = open('201452018_output.txt','w+')     # output file 
		N=len(fnmatch.filter(os.listdir('/home/manish/Desktop/Files'), '*'))  # length of the corpus
		#print(N)
		with open('postingdic_eng.p', 'rb')as f:          
			dic=pickle.load(f)           # load posting lists in dic
		#print(dic.keys())
		#term=input("enter your query")
		query=open("en.topics.126-175.2011.txt", "r").read()       # read query file
		titlestrpos = [x.start()+len("<title>") for x in re.finditer("\<title>",query)] # extract the postion of title tag
		titleendpos = [x.start() for x in re.finditer("\</title>",query)]              # extract the position of title ending tag
		descstrpos =  [x.start()+len("<desc>") for x in re.finditer("\<desc>",query)] # extract the positon of desc starting tag
		descendpos =  [x.start() for x in re.finditer("\</desc>",query)]              # extract the ending position of desc tag 
		titles=[query[a:b] for a,b in zip(titlestrpos, titleendpos)]                  #extract the title field and store in a list(starting pos-ending pos)
		descs=[query[a:b] for a,b in zip(descstrpos, descendpos)]                     # extract the desc field and store it in a list
		que=[a+" "+b for a,b in zip(titles,descs)]                                    # add title and desc to form query and store in a list
		q=0                     # to count query num
		for o in que:   # traverse in query list
			q=q+1
			dicout={}   # to store cosine similarity
			text=IRIndexing.remove_punctuation(self, o)  
			text1=IRIndexing.stop_stem(self, text)
			final=set(text1)
			wunique=list(final)      # final unique set of word in a query
			#print(wunique)
			#print("\n")
			for i in wunique:       # traverse to every word
			 	if i in dic:      
			 		#print("yes")
			 		m=text1.count(i) # tf in that query
			 		length_dict = {key: value for key, value in dic[i].items()} # posting list corrospond to term
			 		length=len(length_dict)  # df
			 		#print(length)
			 		#print("\n")
			 		idf=math.log(N/length) #idf
			 		#print(idf)
			 		#print("\n")
			 		for j in dic[i]:  #cosine similarity
			 			w=(dic[i][j]*idf)*(m*idf) 		
			 			if j in dicout:
			 				c=dicout[j]
			 				c=c+w
			 				dicout[j]=c      
			 			else:
			 				dicout[j]=w 

			d_view= sorted(dicout, key=dicout.get, reverse=True)
			# #d_view.sort(reverse=True)
			rank=0 # trace the rank of each doc
			for i in d_view:
				rank+=1
				f.write(str(q)) #write query num
				f.write(" ") 
				f.write("q0" + " ")
				f.write(str(i)) #write doc id
				f.write(" ")
				f.write(str(rank)) #write rank
				f.write(" ")
				f.write(str(dicout[i])) #write cosine simialrity score
				f.write("/n")
			 	 	

if __name__ == "__main__":
	obj = Tfqu()
