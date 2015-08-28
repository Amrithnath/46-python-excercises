#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mylst=input("please enter the list to be searched\n")
	mymem=input("please enter the value to be searched for\n")
	start=time.time()
	ans=is_member(mymem,mylst)
	print("does the value '"+str(mymem)+"' belong to "+str(mylst)+" ?\n"+str(ans))
	print("time taken:",time.time()-start)
def is_member(x,a):
	for element in a:
		if(str(x)==str(element)):
			return True
	return False
	
if __name__=='__main__':
	main()
	
