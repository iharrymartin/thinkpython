import sys
import string
def capitalised_nested(x):
 c = []
 for s in x:
     c.append(s.capitalize())
 print c
print ' enter the elements of list each seperated by a space'
a = raw_input()
b = string.split(a)
capitalised_nested(b)
if __name__ == "capitalised_nested":
 capitalised_nested(x)
