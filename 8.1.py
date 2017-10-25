import sys 
def backward(x): 
 y = x[::-1]
 for char in y:
	print char
print 'enter the string'
a = raw_input()
backward(a)
if __name__ == "__backward__":
 backward(a)
