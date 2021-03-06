#!/usr/bin/env python

#import xml.etree.ElementTree as ET
import lxml
import json
import sys
import string
import glob                                       # to read folder of documents
from lxml import etree
class IRIndexing():
	def __init__(self):
		self.exclude = list(string.punctuation)       
		self.exclude.append('।')
		path = '/home/manish/Desktop/hindi/*.txt' #path to txt documents
		fileName = glob.glob(path)                # load all txt files into fileName
		posting=dict()                            # dictonary to store term and id of appearing documents
		docid={}                                  # dictonary to give id to each document
		termfreq={}                               # dict to store term freq
		inb=0
		for i in fileName:
			docid[i]=i[-9:-4]                     # give id-last 5 letters of file name(like '00001')
			text=''
			text1=''
			text2=''
		
			try:
				#tree = ET.parse(i)
				#root = tree.getroot()
				root = etree.parse(i)                  #parse to every document
				text1=root.find('title').text          # read title of every doc
				text2=root.find('content').text        # read content field of every doc
				"""for k in root.findall('title'):
					text1 = k.text              # read title
				for k in root.findall('content'):
					text2 = k.text   # read content"""
				text = text1 + text2                   # take title and content into one string
				text = self.remove_punctuation(text)   # function to remove punctuations
				tex = self.remove_stop_word(text)      # function to remove stopwords
				final= self.do_stemming(tex)           # function for stemming
				ls = set(final)                        # remove duplicates
				wordUnique = list(ls)                  # list of unique words

			except lxml.etree.XMLSyntaxError :         # to handle error while parsing
				inb+=1

			for k in range(len(final)):                # traverse in final list to count frequency of each term
				if not final[k] in termfreq:           
					termfreq[final[k]]=1
				else:
					termfreq[final[k]]+=1

				

				
			for j in wordUnique:                      # traverse to every term
				if j in posting:                      # traverse it dict and check
					posting[j].append(docid[i])       # if j is already there, append the posting list with doc id in which term is appearing
				else:
					posting[j]=[docid[i]]             # else add j as key and docID as value

   		
		with open('postinglist.json', 'wt') as f:     # serialising  posting list into json file
			json.dump(posting, f)
			  
		with open('termfrequecy.json', 'wt') as f:    # serialising termfreq into json file
			json.dump(termfreq, f)
    	
    	#----------------------------------------------functions--------------------------------------------------------------------------------------------------------------------------

	def remove_stop_word(self, text):    # stopword function
		stopWord=open("stopWords.txt", "r").read().split("\n")
		text3 = []
		#print(stopWord)
		text = text.split()
		for i in text:
			if i not in stopWord:
				text3.append(i)
		return text3


	def remove_punctuation(self, text):    # punctuation function
		exclude = list(string.punctuation)
		exclude.append('।')
		text = "".join(i for i in text if i not in exclude)
		return text



	def do_stemming(self, word):    # stemming function
		word = [self.stem_word(i) for i in word]
		return word



	def stem_word(self,word):  # stemming function
		suffixes = {
			1: ["ो","े","ू","ु","ी","ि","ा"],
			2: ["कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें"],
			3: ["ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं"],
			4: ["ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां"],
			5: ["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां"],
		}

		for i in 5, 4, 3, 2, 1:
			if len(word) > i + 1:
					
				for sf in suffixes[i]:
						
					if word.endswith(sf):
						return (word[:-i])
			
		return word


if __name__ == "__main__":
	obj = IRIndexing()   # object to class
	