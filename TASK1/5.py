s1=str(input())
s2=str(input())
l1=len(s1)
l2=len(s2)
list1=[]
list2=[]
list1.append(s1[0:(l1//2)+1])
list1.append(s2[0:(l2//2)])
list2.append(s1[l1//2:l1])
list2.append(s2[l2//2:l2])
print(list1,list2)

