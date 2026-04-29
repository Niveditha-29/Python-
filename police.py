'''n = int(input())
events = list(map(int, input().split()))
officers = 0       
untreated = 0      
for event in events:
    if event == -1:  
        if officers > 0:
            officers -= 1  
        else:
            untreated += 1  
    else: 
        officers += event
print(untreated)
'''
n=int(input())
police,unsolved=0,0
events=list(map(int,input().split()))
for i in events:
    if e==-1:
        if police>0:
            police-=1
        else:
            unsolved+=1
    else:
        police+=1
print(unsolved)
