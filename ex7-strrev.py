#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	given=input("enter the sentence or word to be reversed\n")
	start=time.time()
	rev=reverse(given)
	print ("\n\nthe reversed string is\n\n"+rev)
	print("\ntime taken:",time.time()-start)
def reverse(data):
	i=len(data)-1
	rev=""
	for letter in data:
		rev=rev+data[i]
		i=i-1
	return rev
if __name__=='__main__':
	main()
