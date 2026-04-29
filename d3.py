
#max element
l=[2,2,2,1,2,1,1,2,3,2,2,2,3,3,4]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=0
ele=0
for i in d:
    if d[i]>m:
        m=d[i]
        ele=i
print(ele)
