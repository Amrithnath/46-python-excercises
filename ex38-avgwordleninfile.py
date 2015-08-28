#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	err=time.time()
	#try:
	if len(sys.argv)>0:
		filein=sys.argv[1]
	else:
		filein=input("please enter the file name with extension")
	infile=open(filein,'r')
	avglengthfinder(infile)
	'''except:
		print("please enter a valid file name with extension,program will restart in 10 secs")
		while(time.time()-err<10):
			pass
		main()
'''
def avglengthfinder(data):
	lwords=[]
	for line in data:
		tmp=line.split(" ")
		lwords.append(map(lambda a:len(a),tmp))
	avg=0
	n=0
	for element in lwords:
		for number in element:
			n=n+1
			avg=avg+number
	print n
	avg=avg/n
	print "average of all the words given in the file is:",avg
if __name__=='__main__':
	main()
		
