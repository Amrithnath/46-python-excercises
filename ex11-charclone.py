  #!/usr/bin/python
import sys
import os
import time
def main():
	os.system('clear')
	mychar=input("Give me the charater to clone??\n")
	mynum=input("How many times should i clone '"+mychar+"' ?\n")
	start=time.time()
	print(generate_n_chars(mynum,mychar))
	print("time taken:",time.time()-start)
def generate_n_chars(n,x):
	i=0
	ans=" "
	for i in range(n):
		ans=ans+x
	return ans
if __name__=='__main__':
	main()
	
