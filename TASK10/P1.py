class Solution(object):
    def traprainwater(self, height):

        n = len(height)
        left_max = [0] * n
        for i in range(n):
            left_max[i] = max(left_max[i - 1], height[i])

        summ = 0
        right_max = 0
        for j in range(n - 1, 0, -1):
            summ += max(min(left_max[j - 1], right_max) - height[j], 0)
            right_max = max(right_max, height[j])

        return summ
    height=list(map(int,input().split()))
    print(traprainwater(height,height))