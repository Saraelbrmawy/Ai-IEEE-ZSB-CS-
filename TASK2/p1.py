l1=list(map(int,input().split()))
s=sorted(l1)
print(s)
n=int(input())
l2=[i for i in range (len(s)) if s[i]==n]
print(l2[0],l2[-1])