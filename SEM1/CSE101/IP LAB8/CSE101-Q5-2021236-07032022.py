n=input()
lst_n=[int(x) for x in input().split()]
lst_n.sort()
d=input()
l1=[]
l2=lst_n.copy()
f=False
for i in range(len(lst_n)):
	l1.append(lst_n[0])
	l2.remove(lst_n[0])
	lst_n.remove(lst_n[0])
	if(abs(sum(l1)-sum(l2))!=eval(d)):
		continue
	else:
		print("Yes")
		f=True
		break
if(not f):		
	print("No")		

