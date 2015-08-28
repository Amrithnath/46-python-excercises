#!/usr/bin/python
from random import randint
from itertools import permutations
from time import sleep
def main():
    clrlst=['red','brown','black','yellow','green','blue']
    print("Hello shall we play a game of anagrams?")
    sleep(1)
    print("Its something like jumbled words.Its very simple, i give you a jumbled word and you guess the word, \n sounds easy right? \lets see how you fare")
    sleep(3)
    print("A clue to make it easier : The word is a colour")
    clrlist=['red','blue','white','black','yellow','brown','green']
    res=start_game(clrlist)
    while not res==1:
        if res==2:
            print("yay yoou win")
            opt=input("do you want play again???y/n")
            if opt=='y':
                start_game(clrlist)
            else:
                continue
        else:
            break
    print"cya later"
def start_game(mylst):
    print("setting up word and its anagaram")
    myword,anag=get_word_ana(mylst)
    usrgss=''
    while not usrgss == myword:
        print"\n guess the original wordfrom this anagram:{}.".\
                 format(anag)
        usrgss=input("so whats the word?")
        print('press x to exit')
        if not usrgss=='':
            if set(usrgss).issubset(set(myword))and len(usrgss)==len(myword):
                if usrgss==myword:
                    print'Yay you won'
                    sleep(1)
                    return 2
                else:
                    print 'Incorrect,never mind try again'
                    sleep(1)
                continue
            else:
                if not usrgss=='x':
                    print("incorrect your letters must contain words from the given anagram only, please try again")
                    continue
                else:
                    print("the word was :{}".\
                          format(myword))
                    return 1
        else:
            print("your letter must contain only and all letters from the anagram given")
            continue
        return 2
def get_word_ana(data):
    element=''
    if element in data:
        data.remove(element)
    while True:
        element=data[randint(0,len(data))]
        itera=permutations(element)
        for count,itea in enumerate(itera):
            ana_wrd=''.join(list(itea))
            print ana_wrd
            if(not ana_wrd==element and not ana_wrd in data):
                return element,ana_wrd
if __name__=='__main__':
    main()
        
