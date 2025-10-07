from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        j=0
        for i in range(1,n):
            if(nums[j]!=nums[i]):
                j=j+1
                nums[j] = nums[i]
        return j+1

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 1, 2]
    solution = Solution()
    result1 = solution.removeDuplicates(nums1)
    print(f"Example 1: nums = {nums1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result2 = solution.removeDuplicates(nums2)
    print(f"Example 2: nums = {nums2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a sorted list of numbers separated by spaces (e.g., 1 1 2 2 3): ")
        user_nums = list(map(int, user_nums_str.split()))

        user_result = solution.removeDuplicates(user_nums)
        print(f"User Input: nums = {user_nums}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")