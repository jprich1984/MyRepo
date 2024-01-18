
import sys

def Squares(n,fn=lambda x: x**2):
	
	return [fn(i) for i in range(n)]

print(Squares(int(sys.argv[1])))		
