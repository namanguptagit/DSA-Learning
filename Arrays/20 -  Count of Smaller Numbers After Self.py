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

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1 - Brute Force Approach
    nums1 = [5, 2, 6, 1]
    solution1 = Solution()
    result1 = solution1.countSmaller(nums1)
    print(f"Example 1 (Brute Force): nums = {nums1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2 - Brute Force Approach
    nums2 = [-1]
    result2 = solution1.countSmaller(nums2)
    print(f"Example 2 (Brute Force): nums = {nums2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3 - Brute Force Approach
    nums3 = [-1, -1]
    result3 = solution1.countSmaller(nums3)
    print(f"Example 3 (Brute Force): nums = {nums3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 1 - Better Time Complexity Approach
    nums4 = [5, 2, 6, 1]
    solution2 = Solution()
    result4 = solution2.countSmaller(nums4)
    print(f"Example 1 (Better TC): nums = {nums4}")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 2 - Better Time Complexity Approach
    nums5 = [-1]
    result5 = solution2.countSmaller(nums5)
    print(f"Example 2 (Better TC): nums = {nums5}")
    print(f"Output: {result5}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., 5 2 6 1): ")
        user_nums = list(map(int, user_nums_str.split()))

        user_result = solution2.countSmaller(user_nums)
        print(f"User Input: nums = {user_nums}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")