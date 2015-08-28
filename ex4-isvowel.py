#!/usr/binn/python
import sys
import os
import time
def main():
	os.system('clear')
	mydata=input('enter any character \n')	
	progstart(mydata)
def progstart(mydata):
	start=time.time()
	boole=isvowel(mydata)
	print("data entered is vowel ",boole)
	print("time taken:",time.time()-start)
def isvowel(a):
	vowel=['a','e','i','o','u']
	for letter in vowel:
		if(a==letter):
			return True
	return False
if __name__=='__main__':
	main()

