import sys
import string
def nested_sum(x,y):
 e = [x,y]
 print e
print 'enter the elements of list 1 each seperated by a space'
a = raw_input()
b = string.split(a)
print 'enter the elements of list 2 each seperated by a space'
c = raw_input()
d = string.split(c)
nested_sum(b,d)
if __name__ == "nested_sum":
 nested_sum(x,y)
