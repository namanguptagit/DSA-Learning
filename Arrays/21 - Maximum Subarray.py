# Kadane's Algorithm - Optimal Approach
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < cs+nums[i]:
                cs = cs+nums[i]
            else:
                cs = nums[i]
            ans = max(cs,ans)
        return ans
# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1 - Kadane's Algorithm (Optimal)
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution1 = Solution()
    result1 = solution1.maxSubArray(nums1)
    print(f"Example 1 (Kadane's): nums = {nums1}")
    print(f"Output: {result1}")
    print("-" * 30)

    # Example 2 - Single element
    nums2 = [1]
    result2 = solution1.maxSubArray(nums2)
    print(f"Example 2 (Kadane's): nums = {nums2}")
    print(f"Output: {result2}")
    print("-" * 30)

    # Example 3 - All negative numbers
    nums3 = [-5, -2, -8, -1]
    result3 = solution1.maxSubArray(nums3)
    print(f"Example 3 (Kadane's): nums = {nums3}")
    print(f"Output: {result3}")
    print("-" * 30)

    # Example 4 - All positive numbers
    nums4 = [1, 2, 3, 4, 5]
    result4 = solution1.maxSubArray(nums4)
    print(f"Example 4 (Kadane's): nums = {nums4}")
    print(f"Output: {result4}")
    print("-" * 30)

    # Example (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., -2 1 -3 4): ")
        user_nums = list(map(int, user_nums_str.split()))

        user_result = solution1.maxSubArray(user_nums)
        print(f"User Input: nums = {user_nums}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")