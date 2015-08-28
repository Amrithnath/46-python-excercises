#!/usr/bin/python
import os
import sys
import time
import re
def main():
	os.system('clear')
	myword=input("enter a verb")
	start=time.time()
	presentp=make_ing_form(myword)
	print("present participle person form of verb is\n"+presentp)
	print "time taken:",time.time()-start
def make_ing_form(myinp):
	myinp.strip()
	myinp.lower()
	l=len(myinp)-1
	new=""
	if(myinp.endswith('e') and not(myinp.endswith('ie'))):
		if(myinp=="see" or myinp=="be" or myinp=="flee" or myinp=="knee"):				
			for i in range(l+1):
				new=new+myinp[i]
		else:
			for i in range(l):
				new=new+myinp[i]
			
		new=new+"ing"	
	elif(myinp.endswith('ie')):
		for i in range(l-1):
			new=new+myinp[i]	
		new=new+"y"+"ing"
	elif(l==2 and re.match(r'[aeiou]',myinp[1],)):
		for i in range(l+1):
			new=new+myinp[i]
		new=new+myinp[2]+"ing"
	else:
		myinp=myinp+"ing"
		return myinp
	return new
if __name__=='__main__':
	main()
