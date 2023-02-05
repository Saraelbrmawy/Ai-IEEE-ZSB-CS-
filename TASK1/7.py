
List =list(input().split())
n = int(input())
if n>len(List):
	n = int(n%len(List))
List = (List[-n:] + List[:-n])

print(" List after rotation = ",List)