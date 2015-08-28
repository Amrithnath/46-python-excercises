#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	given=input("enter the sentence to be ckecked\n")
	start=time.time()
	res=is_palindrome(given)
	print "the string is a palindrome?\n"+str(res)
	print("\ntime taken:",time.time()-start)
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

	print rev
	if (rev==data):

		return True
	else:
		return False
if __name__=='__main__':
	main()
