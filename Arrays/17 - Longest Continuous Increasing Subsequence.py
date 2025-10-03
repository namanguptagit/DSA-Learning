class Solution:
    def findLengthOfLCIS(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 1
        l = 1 
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                l += 1
                longest = max(longest, l)
            else:
                l = 1
        return longest