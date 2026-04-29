'''l=[2,5,6,2,1,9,8]
sum=0
for i in range(len(l)):
    if i%2!=0 and l[i]%2==0:
        sum=sum+l[i]
print(sum)'
'''
'''l=[2,1,3,2,1,1,3,2]
print(l[:3])
'''
l=[2,1,3,2,1,1,3,2]
res=[]
for i in l:
  if i not in res:
    res.append(i)
print(res)
 

