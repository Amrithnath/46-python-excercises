#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mywrdlst=input("please enter a list of words")
	mynum=input("please enter an integer")
	start=time.time()
	myfltrd=filter_long_words(mywrdlst,mynum)
	print("the filtered list is :",myfltrd)
	print("time taken:",time.time()-start)
def filter_long_words(mylst,mynum):
	newlst=filter(lambda x:len(x)<mynum,mylst)
	return newlst
if __name__=='__main__':
	main()
