#!usr/bin/python
import sys
import os
import time
def main():
	err=time.time()
	try:	
		os.system('clear')
		a=int(input('Enter the 1st number'))
		b=int(input('Enter the 2nd number'))
		c=int(input('Enter the 3rd number'))
		os.system('clear')
		progstart(a,b,c)
	except:
		print("please enter a number (integers for u nerdz) , invalid input detected program will restart in 10 secs")
		while(time.time()-err<10):
			pass
		main()
def progstart(a,b,c):
	start=time.time()
	grtr=max_of_three(a,b,c)
	if(grtr==(a-b-c)):
		print("All three numbers are equal")
		print('time taken:',time.time()-start)
	else:
		print("the greatest number is "+str(grtr))
		print('time taken:',time.time()-start)
def max_of_three(x,y,z):
	if((x==y)and(x==z)):
		return (x-y-z)
	elif((x>y) and (x>z)):
		return x
	elif((y>x)and(y>z)):
		return y
	else:
		return z

if __name__=='__main__':
	main()
