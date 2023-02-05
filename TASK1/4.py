def solution(s1, target):
    n = len(s1)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s1[i] + s1[j] == target:
                print(f" {i} and {j}")
solution([1,4,5,6,8],5)
