#!/usr/bin/python
import os
import sys
import time
def main():
	os.system('clear')
	myword=input("enter a verb")
	start=time.time()
	p3rd=make_3sg_form(myword)
	print("3rdd person form of verb is\n"+p3rd)
	print "time taken:",time.time()-start
def make_3sg_form(myinp):
	myinp.strip()
	myinp.lower()
	l=len(myinp)-1
	new=""
	if(myinp.endswith('y')):
		for i in range(l):
			new=new+myinp[i]
		new=new+"ies"	
	elif(myinp.endswith('o') or myinp.endswith('x') or myinp.endswith('z') or myinp.endswith('s') or myinp.endswith('sh') or myinp.endswith('ch')):
		if(myinp.endswith('o') or myinp.endswith('x') or myinp.endswith('z') or myinp.endswith('s')):
			for i in range(l+1):
				new=new+myinp[i]
		else:
			for i in range(l+1):
				new=new+myinp[i]
		new=new+"es"
	else:
		myinp=myinp+"s"
		return myinp
	return new
if __name__=='__main__':
	main()
