#!/usr/bin/python
import sys
import os
import time
def fileinp():
	mydata=[]
	if(len(sys.argv)>1):
		filein=sys.argv[1]
	else:
		filein=input("please enter the file name with extension")
	
	ifile=open(filein,'r')
	for line in ifile:
		mydata.append(line)
		
	return mydata
def is_palindrome(data):
	data=(data.strip()).lower()
	rev=""
	for letter in data:
		if(letter.isalpha()):		
			data=data
		else:
			data=data.replace(letter,"")
	i=len(data)-1
	for letter in data:
		rev=rev+data[i]
		i=i-1
	
	if (rev==data):

		return True
	else:
		return False
	
def main():
	os.system('clear')
	mylines=fileinp()
	start=time.time()
	print ("the palindromes in the given file are")
	for element in mylines:
		boole=is_palindrome(element)
		if(boole==True):
			print element
	print "time taken:",time.time()-start
if __name__=='__main__':
	main()
	
	
