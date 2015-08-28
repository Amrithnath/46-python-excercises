#!/usr/bin/python
import sys
import os
import time
def find_longest_word():
	os.system('clear')
	mylst=input("please enter the list of words")
	start=time.time()
	lenlst=wordlength(mylst)
	longword=max_in_list(lenlst)
	print("list of legnth of words in list :\n",longword)
	print("time taken:",time.time()-start)
def wordlength(x):
	lst=[]
	for element in x:
		i=0
		for letter in element:
			i=i+1
		lst.append(i)
	return lst
def max_in_list(x):
	ans=x[0]	
	for element in x:
		if(element>ans):
			ans=element
	return ans
if __name__=='__find_longest_word__':
	find_longest_word()
	
	
