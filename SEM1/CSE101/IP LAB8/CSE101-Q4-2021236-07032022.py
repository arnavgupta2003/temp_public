lst=[int(x) for x in input("Enter list").split()]
r=int(input("Enter r"))
lst.sort()
ans=[]
def fn(s,idx,n_s):
	if(idx==len(s)):
		if(len(n_s)==r):
			temp=[]
			for i in n_s:
				temp.append(eval(i))
			ans.append(temp)	

			return
	else:
		fn(s,idx+1,n_s+str(s[idx]))
		fn(s,idx+1,n_s)		
s=""
for i in lst:
	s+=str(i)
fn(s,0,"")	
print(ans)