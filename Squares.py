
import sys
"""Calculates the perfect squares up to a provided number"""

def squares(n,fn=lambda x: x**2):
	
	return [fn(i) for i in range(n)]

def square(n):
	return n**2
print(squares(int(sys.argv[1])))		
