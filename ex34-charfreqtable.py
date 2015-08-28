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
	infile=open(filein,'r')
	for line in infile:
		data.append(line)
	return data
def char_freq_table(myin):
	myresdict={}
	myresdict.clear()
	for element in myin:
		for letter in element:
			i=0
			for check in element:
				if(letter == check):
					i=i+1
			updict={letter:i}
			myresdict.update(updict)
	print("character\tfrequency")
	for sortedValue in sorted(myresdict):
		print(sortedValue+"\t\t"+str(myresdict[sortedValue]))
		
def main():
	os.system('clear')
	myline=fileinp()
	start=time.time()
	char_freq_table(myline)
	print("time taken:",time.time()-start)
		
if __name__=='__main__':
	main()
