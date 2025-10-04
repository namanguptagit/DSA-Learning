# Brute Force Approach But not submitted in leetcode
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n= len(nums)
        res=[]
        for i in range (0,n):
            x = nums[i]
            count = 0
            for j in range (i+1,n):
                if nums[i] > nums[j]:
                    count += 1
            res.append(count)
        return res
# Another Approach Better Time Complexity by sorted array

from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()    
        output = []
        
        for n in nums[::-1]:
            ans = s.bisect_left(n)
            
            output.append(ans)
            s.add(n)
        return list(reversed(output))

# will work on another approach later using fenwick tree