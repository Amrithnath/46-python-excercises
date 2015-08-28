#!/usr/bin/python
import sys
import os
import time
def fileinp():
	data=[]
	if(len(sys.argv)>1):
		filein=sys.argv[1]
	else:
		filein=input("please enter the file name with extension")
	
	fileop=open(filein,'r')
	for line in fileop:
		data.append(line.strip())
	return data
def semordpalin(mydata):
	for word in mydata:
		rev=word[::-1]
		if rev in mydata:
			print(word+" "+rev)

def main():
	os.system('clear')
	mytext=fileinp()
	start=time.time()
	semordpalin(mytext)
	print("time taken:",time.time()-start)
if __name__=='__main__':
	main()
		
	
