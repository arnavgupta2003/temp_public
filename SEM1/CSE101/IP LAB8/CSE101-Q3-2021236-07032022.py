def fn(n,x,y,t,u,v):
	l=abs(x-u)
	d=abs(y-v)
	if(l+d<=t):
		print("Yes")
	else:
		print("No")				
fn()		
#Not working