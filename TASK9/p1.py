class Solution:
    def replaceElements(self, arr):
        for i,num in enumerate(arr):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i + 1:])

        return arr
    arr=list(map(int,input().split()))
    print(replaceElements(arr,arr))