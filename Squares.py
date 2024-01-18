
import sys
"""Calculates the perfect squares up to a provided number"""

def Squares(n,fn=lambda x: x**2):
	
	return [fn(i) for i in range(n)]
print(Squares(int(sys.argv[1])))		
