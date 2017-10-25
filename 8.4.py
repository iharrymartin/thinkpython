import sys
def find(word,letter,index):
 while index < len(word):
	if word[index] == letter:
		return index
	index = index + 1
 return -1
print 'enter the word'
a = raw_input()
print 'enter the letter'
b = raw_input()
print 'enter the index'
c = '3'
print find(a,b,c) 
if __name__=="__find__":
 find(a,b,c)
