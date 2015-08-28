#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mywordarr=input("please give me a list of words\n")
	start=time.time()
	longest=find_longest_word(mywordarr)
	print("the longest word in the given list was:"+longest)
	print"time taken:",time.time()-start
def find_longest_word(mydata):
	longe=reduce(lambda x,y: (x if(len(x)>len(y)) else y),mydata)
	return longe
if __name__=='__main__':
	main()
