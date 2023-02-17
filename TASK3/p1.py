def mean(lst):
    n = len(lst)
    getsum = sum(lst)
    Mean = getsum / n
    return Mean
def median(lst):
    lst2 = sorted(lst)
    n=len(lst)
    if n % 2 == 0:
        med1 = lst2[n // 2]
        med2 = lst2[n // 2 - 1]
        Median = (med2 + med1) / 2
    else:
        Median = lst2[n //2]
    return  Median
def mode (lst):
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return max(dic,key=dic.get)

try:
    lst = list(map(int,input().split()))
    print("mean:%0.3f" % mean(lst))
    print("median: ", median(lst))
    print("mode:",mode(lst))
except ValueError as ex:
    print(" enter an integer number: ")
