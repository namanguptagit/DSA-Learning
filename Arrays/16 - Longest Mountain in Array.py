class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 0
        
        for i in range(1, n-1):
            # check if arr[i] is a peak
            if arr[i-1] < arr[i] > arr[i+1]:
                l, r = i, i
                # expand left
                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1
                # expand right
                while r < n-1 and arr[r] > arr[r+1]:
                    r += 1
                # update max
                longest = max(longest, r - l + 1)
        
        return longest