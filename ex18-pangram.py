#!/usr/bin/python
import sys
import os
def main():
	os.system('clear')
	mysent=input("enter the sentence")
	mysent=mysent.lower()
	mysent=mysent.replace(" ","")
	
	if(len(mysent)<26):
		a=False
		output(a)
	else:
		a=ispangram(mysent)
		output(a)
def output(a):
	print ("A pangram is a sentence that contains all the english alphabet")
	print ("Is the sentence a pangram?\n",str(a))
def ispangram(x):
	alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
	for alpha in alp:
		if(str(x).find(alpha)<0):
			return False
		else:
			ans=True
	return ans
if __name__=='__main__':
	main()
	
