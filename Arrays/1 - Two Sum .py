from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = {}
        for i in range(0, n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining], i]
            hash_map[nums[i]] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        left = 0
        right = n - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return -1
# Add code below this line to test your solution    
if __name__ == "__main__":
    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    solution = Solution()
    result1 = solution.twoSum(nums1, target1)
    print(f"Example 1: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Example 2: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., 3 5 7 9): ")
        user_nums = list(map(int, user_nums_str.split()))

        # Take target input
        user_target = int(input("Enter the target number: "))

        user_result = solution.twoSum(user_nums, user_target)
        print(f"User Input: nums = {user_nums}, target = {user_target}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

