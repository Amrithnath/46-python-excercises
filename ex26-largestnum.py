#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mylst=input("please enter the list of numbers")
	start=time.time()
	maxno=max_in_list(mylst)
	print("max number in list is :",maxno)
	print "time taken:",time.time()-start
def max_in_list(mydata):
	x=reduce(lambda a,b: (a if (a>b) else b), mydata)
	return x
if __name__=='__main__':
	main()
