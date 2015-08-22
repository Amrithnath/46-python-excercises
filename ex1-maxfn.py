#!usr/bin/python
import sys
import os
import time
def main():
	err=time.time()
	os.system('clear')
	try:
		a=int(input("enter a random number  "))
		b=int(input("enter a 2nd random number  "))
		os.system('clear')
		progstart(a,b)
	except ValueError:
		print("please enter integers(numbers for u normal people) only program will restart in 10secs")
		while((time.time()-err)<10):
			pass
		main()
def progstart(a,b):	
	start=time.time()
	c=max(a,b)
	if(c==(a-b)):
		print('Both the numbers entered are equal')
		print 'time taken:',time.time()-start
	else:
		print('the greater of the 2 numbers is:'+str(c))
		print 'time taken:',time.time()-start
def max(x,y):
	if(x>y):
		return x
	elif(x<y):
		return y
	else:
		return(x-y)

if __name__=='__main__':
	main()

