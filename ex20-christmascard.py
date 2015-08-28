#!/usr/bin/python
#!/coding=utf-8
import os
import sys
import time
def main():
	os.system('clear')
	lsteng=input("enter a list of english words")
	start=time.time()
	lstswe=translate(lsteng)
	print("the list given translated to swedish")
	print(lstswe)
	print("time taken:",time.time()-start)
def translate(mylst):
	myswedict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
	mynewlst=[]
	for element in mylst:
		if(myswedict.has_key(element)):
			mynewlst.append(myswedict[element])
	return mynewlst
if __name__=='__main__':
	main()	
