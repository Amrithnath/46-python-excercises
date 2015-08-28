#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mytext=input("enter the text to scan for frequency")
	start=time.time()
	myfreqdict=char_freq(mytext)
	print("frequency of each character in text is")
	print(myfreqdict)
	print("time taken:",time.time()-start)
def char_freq(mydata):
	myresdict={}
	for element in mydata:
		i=0
		for check in mydata:
			if(element==check):
				i=i+1
		updict={element:i}
		myresdict.update(updict)
	return myresdict
if __name__=='__main__':
	main()
