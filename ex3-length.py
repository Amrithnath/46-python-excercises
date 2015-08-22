#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mydata=input('enter the data \n')
	print('\n')
	start=time.time()
	lent=length(mydata)
	print("length of the given data is "+str(lent))
	print('time taken:',time.time()-start)
def length(given):
	i=0
	for char in given:
		i=i+1
	return i
if __name__=='__main__':
	main()
