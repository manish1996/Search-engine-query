import sys
import sys
import xml.etree.ElementTree as ET # etree library for xml data parsing
f4 = open("wordCount.txt", 'r+')  #output file
output=''
allfiles=sys.argv  # commandline input all text files
fileposition=1  # pointer to traverse through all the txt files

while fileposition<len(allfiles):
	tree = ET.parse(allfiles[fileposition])  #read all the document files
	root = tree.getroot()
	for j in root.findall('title'): # find title field
		out1 = j.text
	for k in root.findall('content'): # find content field
		out2 = k.text
	output+= out1 + out2  #string hold all the texts
	fileposition+=1  # increment pointer to access next file
 
 print("removing punctuation")
		exclude = list(string.punctuation)
		exclude.append('।')
		output = "".join(c for c in output if c not in exclude)
print(output) #content of all the files
m= output.split(" ")
n = set(m)
w = list(n) #list of all unique words
for i in range(len(w)):
	f4.write(str(w[i] + '\t\t'))  # write each word in wordCount.txt
	f4.write(str(m.count(str(w[i]))) + '\n') # write number of occurence of each word
	
	"""import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))"""
