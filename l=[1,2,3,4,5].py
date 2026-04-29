'''l=[1,2,3,4,5]
for i in range(1,4):
    l[i-2]=l[i]
for i in range(0,4):
    print(l[i],end=" ")
    '''
'''l=[6,"sashs",3.14,False]
l.insert("Bike")
print(l)
'''
'''l=[6,7,8,9,10,11,12]
l.append(13)
l.extend("nive")
l.pop()
l.extend([15,16,17])
l.remove(9)
print(len(l))
'''
'''l=[6,7,8,9,10,11,12]
for i in l:
    l.remove(i)
print(l)
'''
'''l=[6,7,8,9,10,11,12,13,14,15,16,17]
print(l[2:10:3])
'''
'''l=[6,7,8,9,10,11,12,13,14,15,16,17]
print(l[-3:-1])
'''
l=[1,5,7,4,8,2]
print(int(l[3]+l[5]))
