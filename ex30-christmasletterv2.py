#!/usr/bin/python
#!coding=utf-8
import sys
import os
import time
def main():
	os.system('clear')
	myenglst=input("please enter a list of english words from your christmas letters")
	start=time.time()
	tlst=map(translate ,myenglst)
	print("list of translated words in same order:",tlst)
	print("time taken:",time.time()-start)
def translate(mydata):
	myswedict={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
	return myswedict[mydata]

if __name__=='__main__':
	main()
