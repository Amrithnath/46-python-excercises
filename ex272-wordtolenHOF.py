#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	wrdlst=input("please enter the list of words")
	start=time.time()
	lenlst=Word_to_Length_map_func(wrdlst)
	print("the length of the corresponding words are:",lenlst)
	print"time taken",time.time()-start
def Word_to_Length_map_func(mydata):
	lenlst=map(lambda x:len(x),mydata)
	return lenlst
if __name__=='__main__':
	main()

