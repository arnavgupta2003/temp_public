def fn(n):
	if(n==0):
		return 0
	if(n==1):
		return 0
	if(n==2):
		return 1
	if(n>40):
		return "Upper cap reached"	
	return fn(n-1)+fn(n-2)+fn(n-3)
n=int(input("Enter n"))
print(fn(n))				