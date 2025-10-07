from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = suf = 1
        res = float('-inf')
        n = len(nums)

        for i in range(n):
            pre *= nums[i]
            suf *= nums[n - 1 - i]
            res = max(res, pre, suf)
            if pre == 0: pre = 1
            if suf == 0: suf = 1
        return res

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    nums1 = [2, 3, -2, 4]
    solution = Solution()
    result1 = solution.maxProduct(nums1)
    print(f"Example 1: nums = {nums1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    nums2 = [-2, 0, -1]
    result2 = solution.maxProduct(nums2)
    print(f"Example 2: nums = {nums2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    nums3 = [-2, 3, -4]
    result3 = solution.maxProduct(nums3)
    print(f"Example 3: nums = {nums3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4
    nums4 = [0, 2]
    result4 = solution.maxProduct(nums4)
    print(f"Example 4: nums = {nums4}")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., 2 3 -2 4): ")
        user_nums = list(map(int, user_nums_str.split()))

        user_result = solution.maxProduct(user_nums)
        print(f"User Input: nums = {user_nums}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")