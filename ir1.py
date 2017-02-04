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