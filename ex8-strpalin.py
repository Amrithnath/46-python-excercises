#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	given=input("enter the word to be checked\n")
	start=time.time()
	res=is_palindrome(given)
	print "the string is a palindrome?\n"+str(res)
	print("\ntime taken:",time.time()-start)
def is_palindrome(data):
	i=len(data)-1
	rev=""
	for letter in data:
		rev=rev+data[i]
		i=i-1
	if (rev==data):

		return True
	else:
		return False
if __name__=='__main__':
	main()
