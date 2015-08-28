#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	given=input("enter the list of numbers\n")
	start=time.time()
	tot=sum(given)
	pro=mul(given)
	print("sum="+str(tot))
	print("product="+str(pro))
	print("time taken:",time.time()-start)
def sum(data):
	ans=0
	for num in data:
		ans=ans+num
	return ans
def mul(data):
	ans=1
	for num in data:
		ans=ans*num
	return ans
if __name__=='__main__':
	main()
