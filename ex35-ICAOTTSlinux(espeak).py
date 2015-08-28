#!/usr/bin/python
import sys
import os
import time
def ofile():
	data=[]
	if(len(sys.argv)>1):
		ifile=sys.argv[1]
	else:
		ifile=input("please enter the file name with extension")
	filere=open(ifile,'r')
	for line in filere:
		data.append(line)
	return data
def speak_icao(mytext,TTS):
	print mytext
	icaodict = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     	'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     	'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     	's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     	'x':'x-ray', 'y':'yankee', 'z':'zulu','1':'wun','2':'too','3':'tree','4':'fower','5':'fife','6':'six','7':'sev-	en','8':'ait','9':'niner','0':'zee-ro'}
	for element in mytext:
		wstart=time.time()
		while(time.time()-wstart<1.25):
			pass
		for char in element:
			cstart=time.time()
			while((time.time()-cstart)<0.25):
				pass
			if(not(char.isspace()) and TTS==1):
				os.system('pico2wave'+' '+'-w /tmp/test.wav'+' '+icaodict[char.lower()])
				os.system('aplay'+' '+'/tmp/test.wav')
			elif(not(char.isspace()) and TTS==2):
				os.system('espeak'+' '+icaodict[char.lower()])
def main():
	os.system('clear')
	mydata=ofile()
	TTS=input("which TTS client do you want to use???\n 1) pico -slower but natural  \n 2)espeak -faster but robot like")
	speak_icao(mydata,TTS)
if __name__=='__main__':
	main()

	
	
