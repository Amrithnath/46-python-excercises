#!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mywrdlst=input("please enter a list of words")
	start=time.time()
	mylenlst=Word_to_len_lst_comp(mywrdlst)
	print("the length of the corresponding words are:",mylenlst)
	print("time taken:",time.time()-start)
def Word_to_len_lst_comp(mydata):
	newlst=[len(X) for X in mydata]
	return newlst
if __name__=='__main__':
	main()
