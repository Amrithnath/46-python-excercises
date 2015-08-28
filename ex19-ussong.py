#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	a="bottles of beer on the wall,"
	b="bottles of beer."
	c="Take one down, pass it around,"
	d=" bottles of beer on the wall."
	i=99
	start=time.time()
	while(i>0):
		print(str(i)+a+str(i)+b)
		i=i-1
		print(c+str(i)+d)
		i=i-1
	print("time taken:",time.time()-start)
if __name__=='__main__':
	main() 
