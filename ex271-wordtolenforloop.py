#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	myinparr=input("enter an array of words\n")
	start=time.time()
	mywordlength=wordtolength(myinparr)
	print("the lengths of the corresponding words are:\n",mywordlength)
	print "time taken:",time.time-start
def wordtolength(myinp):
	lengtharr=[]
	for element in myinp:
		lengtharr.append(len(element))
	return lengtharr
if __name__=='__main__':
	main()
