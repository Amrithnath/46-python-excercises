#!/usr/bin/python
import sys
import os
import time
import re
def main():
	os.system('clear')
	err=time.time()
	try:
		if len(sys.argv)>0:
			filein=sys.argv[1]
		else:
			filein=input("please enter the file name with extension")
		infile=open(filein,'r')
		hapax(infile)
	except:
		print("please enter a valid file name with extension,program will restart in 10 secs")
		while(time.time()-err<10):
			pass
		main()
	
def hapax(data):
	words=[]
	mydict={}
	for line in data:
		tmp=line.split(" ")
		words.append(tmp)
	for element in words:
		for key in element:
			if key in mydict:
				mydict[key]+=1
			else:
				newdict={key:1}
				mydict.update(newdict)
	for key in mydict:
		if(mydict[key]==1):
			print key

if __name__=='__main__':
	main()
	
