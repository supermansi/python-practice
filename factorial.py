n=int(input())
def factorial(a):
	if(a==2):
		return 2
	else:
		return a*factorial(a-1)
print(factorial(n))
