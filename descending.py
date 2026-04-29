'''l=[1,5,2,4,3,6,7]
odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort(reverse=True)
res=even+odd
print(res)
'''
l=[1,5,2,4,3,6,7]
res=[]
l.sort()
for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)
