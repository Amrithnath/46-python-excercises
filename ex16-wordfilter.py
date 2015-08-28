#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mylst=input("please enter the list of words")
	mynum=input("please enter the filter value")
	start=time.time()
	lst=filter_long_words(mylst,mynum)
	print("filtered list=",lst)
	print("time taken:",time.time()-start)
def filter_long_words(x,n):
	for element in x:
		if(len(element)<=n):
			x.remove(element)
	return x
if __name__=='__main__':
	main()

			
	
	
