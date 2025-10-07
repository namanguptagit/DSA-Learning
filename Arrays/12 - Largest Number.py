from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def compare(a,b):
            if a+b > b+a :
                return -1
            elif b+a > a+b :
                return 1
            else :
                return 0
        nums.sort(key=cmp_to_key(compare))
        result = ''.join(nums)
        return '0' if result[0] == '0' else result

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    nums1 = [10, 2]
    solution = Solution()
    result1 = solution.largestNumber(nums1)
    print(f"Example 1: nums = {nums1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    nums2 = [3, 30, 34, 5, 9]
    result2 = solution.largestNumber(nums2)
    print(f"Example 2: nums = {nums2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    nums3 = [1]
    result3 = solution.largestNumber(nums3)
    print(f"Example 3: nums = {nums3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4
    nums4 = [10]
    result4 = solution.largestNumber(nums4)
    print(f"Example 4: nums = {nums4}")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., 10 2 3 30 34 5 9): ")
        user_nums = list(map(int, user_nums_str.split()))

        user_result = solution.largestNumber(user_nums)
        print(f"User Input: nums = {user_nums}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")