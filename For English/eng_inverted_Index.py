#!/usr/bin/env python
import lxml
import json
import re
from porter2stemmer import Porter2Stemmer
import sys
import os
import pickle
import string
import glob        
import xml.etree.ElementTree as ET                                 # to read folder of documents
from lxml import etree
stopWord=open("stopwords_en.txt", "r").read().split("\n")
class IRIndexing():
	def __init__(self):
		self.exclude = list(string.punctuation)       
		self.exclude.append('।')
		path = '/home/manish/Desktop/Files/'        # path to txt documents
		posting=dict()
		termfreq={}                                 # dict to store term freq in each doc
		inb=0
		for i in os.listdir(path):  
			 #print(i)  	  
			 filepath = path + i
			 #print(filepath)
			 try:
			 	root = etree.parse(filepath)           #parse to every document
			 except Exception as e:
			 	continue
			# root = tree.getroot()
			 textt=''
			 text1=''
			 text2=''
			 text3=''
			 #for k in root.findall('DOCNO'):
			 #		self.text3 = k.text
			 #print(text3)
			 #for k in root.findall('TITLE'):
			 	#if(root.findall('<TITLE>') != -1):
			 	#	self.text1 = k.text
			# for k in root.findall('TEXT'):
			 #	self.text2 = k.text
			 if(root.find('TITLE')==-1):
			 	text1=root.find('TITLE').text          # read title of every doc
			 text2=root.find('TEXT').text           #read content field of every doc
			 text3=root.find('DOCNO').text 
			 textt = text1 + text2                  # take title and content into one string
			 #print(textt)
			 textt = self.remove_punctuation(textt) # function to remove punctuations
			 final= self.stop_stem(textt)           #function for stemming
			 ls = set(final)                        # remove duplicates
			 wordUnique = list(ls)                  # list of unique words 
			 #print(wordUnique)

			 
                
           
			 #except lxml.etree.XMLSyntaxError :        # to handle error while parsing
			 #	inb+=1
				

			 for k in range(len(final)):               # traverse in final list to count frequency of each term
				 if not final[k] in termfreq:
				 	termfreq[final[k]]=1
				    	
				 else:
					 termfreq[final[k]]+=1

			 for j in wordUnique:                      # traverse to every term
				 post={i:termfreq[j]}                  # dict that contain docid and termfrequency
				 if j in posting:                      # traverse it dict and check
					 posting[j].update(post)           # if j is already there, append the posting dict with post dict
			
				 else:
					 posting[j]=post                   # else add j as key and post dict as its value
			
				
		#print(posting.keys())		
					
				
					

		

		with open('postingdic_eng.p', 'wb') as handle:
			pickle.dump(posting, handle, protocol=pickle.HIGHEST_PROTOCOL)
   		
   		#pickle.dump(posting, open("postingdict_engs.p", "wb"))
		#with open('postingdict_eng.json', 'wt') as f:     # serialising  posting list into json file
		#	json.dump(posting, f)
			  
		#with open('termfrequecy_eng.json', 'wt') as f:    # serialising termfreq into json file
			#json.dump(termfreq, f)
    	
    	#----------------------------------------------functions--------------------------------------------------------------------------------------------------------------------------


	def remove_punctuation(self, text):    # punctuation function
		exclude = list(string.punctuation)
		exclude.append('।')
		text = "".join(i for i in text if i not in exclude)
		return text


	def stop_stem(self, data):
		stemwords = []
		stemmer = Porter2Stemmer()
		data=data.split()
		for word in data:
		  	if word not in stopWord:
		  		stemwords.append(stemmer.stem(word)) 

		#l =list(stemwords)
		return stemwords 

if __name__ == "__main__":
	obj = IRIndexing()   # object to class
	
