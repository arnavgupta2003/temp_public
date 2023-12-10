l=[int(x) for x in input().split()]
def fn_1(l,n):
	if(n==1):
		return l[0]
	return min(l[n-1],fn_1(l,n-1))
ans=[]
sm1=fn_1(l,len(l))
ans.append(sm1)
l.remove(sm1)
ans.append(fn_1(l,len(l)))
print(ans)