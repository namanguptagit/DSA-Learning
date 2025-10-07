from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    solution = Solution()
    result1 = solution.minSubArrayLen(target1, nums1)
    print(f"Example 1: target = {target1}, nums = {nums1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    target2 = 4
    nums2 = [1, 4, 4]
    result2 = solution.minSubArrayLen(target2, nums2)
    print(f"Example 2: target = {target2}, nums = {nums2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    target3 = 11
    nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
    result3 = solution.minSubArrayLen(target3, nums3)
    print(f"Example 3: target = {target3}, nums = {nums3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4 (user input)
    print("Testing with user input...")
    try:
        # Take target input
        user_target = int(input("Enter the target sum: "))
        
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., 2 3 1 2 4 3): ")
        user_nums = list(map(int, user_nums_str.split()))

        user_result = solution.minSubArrayLen(user_target, user_nums)
        print(f"User Input: target = {user_target}, nums = {user_nums}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")