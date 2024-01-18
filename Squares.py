
import sys
"""Calculates the perfect squares up to a provided number"""
def Squares(n):
	L=[]
	for i in range(n):
		L.append(i**2)
	return L

print(Squares(int(sys.argv[1])))		
