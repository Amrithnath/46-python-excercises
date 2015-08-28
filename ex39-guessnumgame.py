#!/usr/bin/python
import sys
import os
import time
import random
def main():
        g=1
        err=time.time()
        #usr_ans=7
        name=input("Hello! What is your name??\n")
        usr_guess=input("Well, %s ,I am thinking of a number between 1 and 20.\nTake a guess.\nRemember you only have 5 guesses"%name)
        mynum=random.randrange(1, 20, 1)
        gimme_inp(g,usr_guess,name,mynum)
        print mynum
def gimme_inp(g,usr_guess,name,mynum):
	ans_dict={1:"pluto",2:"neptune",3:"uranus",4:"saturn",5:"jupiter",6:"mars",7:"earth!!",8:"venus",9:"mercury",10:"sun"}
	usr_ans=game_eng(usr_guess,mynum)
	while(usr_ans!=7):
		if(g>=5):
			end_prog(mynum)
		print("you are at "+ans_dict[usr_ans]+" try again please")
		g=g+1
		usr_guess=input("please enter your guess again\n")
		gimme_inp(g,usr_guess,name,mynum)
	if(usr_ans==7):
		print("Good job, "+name+" ,you guessed my number in "+str(g)+" guesses")
		quit()
def game_eng(inp,mynum):
	if inp==mynum:
		return 7
	else:
		y=mynum
		x=abs(int((20-(y+inp))/2))
		return x
def end_prog(x):
        print("you have exceeded the maximum number of guesses!!! You loose . better luck next time")
        print("the number was:",x)
        quit()
if __name__=='__main__':
	main()
'''	try:
		if(x<=20 and x>=1):
			usr_ans=game_eng(x,mynum)
		else:
			print("please enter a valid integer between 1 and 20,program will restart in 10 seconds")
			while(time.time()-err<10):
				pass		
			gimme_inp(g,name,x,mynum,err)
	except:
		print("please enter a valid integer between 1 and 20,program will restart in 10 seconds")
		while(time.time()-err<10):
			pass		
		gimme_inp(g,name,x,mynum,err)
'''
