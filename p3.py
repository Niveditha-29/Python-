l=[2,2,2,3,3,3,3,4,5,5]
res=[]
for i in l:
    if i not in res and l.count(i)%2!=0:
        res.append(i)
print(res)