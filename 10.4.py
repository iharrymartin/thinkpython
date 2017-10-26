import sys
import string
def middle(x):
 c = x[1:-1]
 print c
print ' enter the elements of the list seperated by a space'
a = raw_input()
b = string.split(a)
middle(b)
if __name__ =="middle":
 middle(x)
