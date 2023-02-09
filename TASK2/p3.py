l1=list(map(int,input().split()))
sum=0
lst1=[]
lst2=[]
l2=sorted(l1)
for i in l1:
    if i<0:
        continue
    sum = sum + i
    lst1.append(i)
print(lst1, sum)
lst2.append(l2[0:2])
print(lst2,l2[0]+l2[1])


