# put your python code here
lst=list(input().split())
lst2=[]

for i in range(len(lst)):
    a,b=lst[i].split('=')

    lst2.append([a,int(b)])
print(lst2)
d=dict(lst2)
print(d)
print(*sorted(d.items()))
