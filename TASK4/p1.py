from math import sqrt
def max_min(lst):
    maximum=max(lst)
    minimum = min(lst)
    r=maximum-minimum
    return maximum,minimum,r
def q2_(lst):
    lst2 = sorted(lst)
    n=len(lst)
    if n % 2 == 0:
        med1 = lst2[n // 2]
        med2 = lst2[n // 2 - 1]
        q2=(med2 + med1) / 2
    else:
        q2 = lst2[n //2]
    return q2
def q1_q3(lst):
    l1 = []
    l2 = []
    lst2 = sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        l1.append(lst2[0:(n // 2 )])
        l2.append(lst2[n //2:])
    else:
        l1.append(lst2[0:(n // 2 )])
        l2.append(lst2[n //2+1:])
    return q2_(l1[0]),q2_(l2[0])
def mean(lst):
    n = len(lst)
    getsum = sum(lst)
    Mean = getsum / n
    return Mean
def variance(lst):
    n = len(lst)
    s=0
    for i in lst:
        v=((i-mean(lst))**2)
        s=s+v
        var=s/n
    return var
if __name__ =='__main__':
    while True:
        try:
            lst = list(map(int, input().split()))
            break
        except ValueError:
            print("Enter a list of number")
    try:
        max1, min1, ran = max_min(lst)
        qu1, qu3 = q1_q3(lst)
        IQR = qu3 - qu1
        standard = sqrt(variance(lst))
        print("min=", min1)
        print("Q1=", qu1)
        print("Q2=", q2_(lst))
        print("Q3=", qu3)
        print("max=", max1)
        print("range=", ran)
        print("IQR=", IQR)
        print("Variance=", "%.4f" % variance(lst))
        print("standard deviation=", "%.3f" % standard)
    except (ZeroDivisionError,ValueError,IndexError):
        print("list is empty")








