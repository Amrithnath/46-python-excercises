#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mylst=input("please enter the list of words")
	start=time.time()
	lenlst=wordlength(mylst)
	print("list of legnth of words in list :\n",lenlst)
	print("time taken:",time.time()-start)
def wordlength(x):
	lst=[]
	for element in x:
		i=0
		for letter in element:
			i=i+1
		lst.append(i)
	return lst
if __name__=='__main__':
	main()
	
	
