
import sys

def Squares(n):
	L=[]
	for i in range(n):
		L.append(i**2)
	return L

print(Squares(int(sys.argv[1])))		
