#!/usr/bin/python
#!coding=utf-8
import sys
import os
import time
def main():
	os.system('clear')
	err=time.time()
	try:
		if len(sys.argv)>0:
			filein=sys.argv[1]
		else:
			filein=input("please enter the file name with extension")
		infile=open(filein,'r')
		filelinemaker(infile)
	except:
		print("please enter a valid file name with extension,program will restart in 10 secs")
		while(time.time()-err<10):
			pass
		main()
def filelinemaker(data):
	i=0
	fileout='line_file.txt'
	ofile=open(fileout,'a')
	for line in data:
		i=i+1
		line=str(i)+" "+line
		ofile.write(line)
		print line
if __name__=='__main__':
	main()
