def countNum(l):
	if not l:
		return 0
	else:
		return 1+countNum(l[1:])

lst=[x for x in input().split()]
print(countNum(lst))			
