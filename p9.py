'''l=[60,10,30,20,40,90,50,70]
n=45
m=75
res=[]
for i in l:
    if i in range(n,m):
        res.append(i)
print(res)
'''
l=[1,2,5,7,6,9,8]
n=1
m=5
res=[]
for i in l:
    if i in range(n*m):
        res.append(i)
print(res)
