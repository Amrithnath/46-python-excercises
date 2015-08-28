import time
def main():
	mylst=input("please enter the list for which you want to perform map, filter and reduce funcions\n")
	fnmp=input("enter the function to be performed for using map function")
	fnflt=input("enter the function to be performed for using filter function")
	fnred=input("enter the function to be performed for using reduce function")
	start=time.time()
	print ("map output:",mapfn(fnmp,mylst))
	print("filter output:",filterfn(fnflt,mylst))
	print("reduce output:",reducefn(fnred,mylst))
	print("time taken:",time.time()-start)
def mapfn(fn,mylst):
	op=[]
	for element in mylst:
		op.append(fn(element))
	return op
def filterfn(fn,mylst):
	op=[]
	for element in mylst:
		if(fn(mylst)):
			op.append(element)
	return op
def reducefn(fn,mylst):
	my1st=mylst[0]
	for mynext in mylst[1:]:
		my1st=fn(my1st,mynext)
	return my1st
if __name__=='__main__':
	main()
