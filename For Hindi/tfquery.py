import json
import os
import tfidf
import fnmatch
import math
from tfidf import IRIndexing
import string
class Tfqu():
	def __init__(self):
		dic={}
		N=len(fnmatch.filter(os.listdir('/home/manish/Desktop/hindi'), '*.txt'))
		with open('postingdict.json')as f:
			dic=json.load(f)
		print(dic.keys())
		term=input("enter your query")
		dicout={}
		text=IRIndexing.remove_punctuation(self, term)
		text1=IRIndexing.remove_stop_word(self, text)
		text2=self.do_stemming(text1)
		final=set(text2)
		wunique=list(final)
		#print(wunique)
		for i in wunique:
			if i in dic:
				print("yes")
				length_dict = {key: value for key, value in dic[i].items()}
				length=len(length_dict)
				print(length)
				idf=math.log(N/length)
				for j in dic[i]:
					w=dic[i][j]*idf
					if j in dicout:
						c=dicout[j]
						c=c+w
						dicout[j]=c      
					else:
						dicout[j]=w 


		sorted_outdic = sorted(dicout, key=dicout.get, reverse=True)
		print(sorted_outdic)

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
	obj = Tfqu()