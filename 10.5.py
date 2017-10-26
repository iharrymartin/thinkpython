import sys
import string
def chop(x):
 c = [x[0],x[-1]]
 print c
print ' enter the elements of the list seperated by a space'
a = raw_input()
b = string.split(a)
chop(b)
if __name__ =="chop":
 chop(x)
