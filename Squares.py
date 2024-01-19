
import sys
import numpy as np
"""Calculates the perfect squares up to a provided number"""

def squares(n,fn=lambda x: x**2):
	
	return [fn(i) for i in range(n)]

def square(n):
	return n**2
print(f'Squares from 0 to {sys.argv[1]}:{squares(int(sys.argv[1]))}')

def sigmoid(x,a=1):
	return 1/(1+np.exp(-a*x))

print(f'Scaled Sigmoid of {sys.argv[1]}: {sigmoid(int(sys.argv[1]))}')	
			
