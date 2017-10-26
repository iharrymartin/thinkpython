import sys
import string
def is_sorted(x,y):  
 if y == x:
  print 'true'
 else:
  print 'false'
print ' enter the elements of the list seperated by a space '
a = raw_input()
b = string.split(a)
c = b
d = c.sort()
is_sorted(b,d)
if __name__ =="is_sorted":
 is_sorted(x,y)
