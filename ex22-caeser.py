#!/usr/bin/python
import sys
import os
import time
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
def main():
	os.system('clear')
	choice=input("do you want to encrypt or decrypt the ROT-13 caser cipher?\n1:encrypt\n2:decrypt\n")
	os.system('clear')
	mydata=input("please enter the data for the required function (encrypt / decrypt)\n")
	start=time.time()
	if(int(choice)==1):	
		usrrqd=ROT_13encdec(mydata)
		print("you requested your data to be encrypted with the caeser ROT-13 cipher")
		print("Your plain text is \n'"+mydata+"'")
		print("Your cipher text is \n'"+usrrqd+"'")
	elif(int(choice)==2):
		usrrqd=ROT_13encdec(mydata)
		print("you requested your data to be decrypted with the caeser ROT-13 cipher")
		print("Your cipher text is \n'"+mydata+"'")
		print("Your plain text is \n'"+usrrqd+"'")

	else:
		i=0
		err=time.time()
		print("you have entered an unsupported input please try again, program will restart in 10 seconds")
		while(int(time.time()-err)<10):
			i=i+1
		os.system('clear')
		main()
	print "time taken:",time.time()-start
def ROT_13encdec(plaintext):
	ciphertext=""
	for element in plaintext:
		if(key.has_key(element)):
			ciphertext=ciphertext+str(key[element])
		else:
			ciphertext=ciphertext+str(element)
	return ciphertext
'''
def ROT_13dec(ciphertext):
	plaintext=" "
	x=[]
	a=key.keys()
	b=key.values()
	i=0
	for element in ciphertext:
		if(element in b):
			
			x.append(a[b.index(element)])
			plaintext=plaintext+str(x[-1])
		else:
			plaintext=plaintext+str(element)
	return plaintext
'''
if __name__=='__main__':
	main()
