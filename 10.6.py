import sys
import string
def is_sorted(x,y):  
 if x == y:
  print 'true'
 else:
  print 'false'
print ' enter the elements of the list continusly '
a = raw_input()
c = string.split(a)
b = sorted(a)
is_sorted(c,b)
if __name__ =="is_sorted":
 is_sorted(x,y)
