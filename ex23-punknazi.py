#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	errline=input("enter the line to be checked and corrected for punctuation\n")
	start=time.time()
	corrline=correct(errline)
	print "corrected\n"+corrline
	print "time taken:",time.time()-start
def correct(myinput):
	op=""
	j=0
	for element in myinput:
		if(element.isspace()):
			if(j==0):
				op=op+element
				j=1
		elif(element=='.'):
			op=op+element+" "		
		else:
			op=op+element
			j=0
	return op
if __name__=='__main__':
	main()
	
