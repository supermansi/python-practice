n=int(input("Enter the number of elements to be dislayed of the Fibonacci series:"))
a=0
b=1
for i in range(0,n):
	c=a+b
	print(a)
	a=b
	b=c
#Tested till value of n=99999
#Timed it but had to interrupt as system heated up
#real	17m16.400s
#user	5m13.156s
#sys	0m9.012s


