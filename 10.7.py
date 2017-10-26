import sys
def anagram(x,y):
 c = sorted(x)
 d = sorted(y)
 if c == d:
	print 'is anagram'
 else:
	print "mot anagram"
print 'enter the elements'
a = raw_input()
print ' enter the elements'
b = raw_input()
anagram(a,b)
if __name__ == "anagram":
 anagram(x,y)
