from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        mid = (len(nums)-1) // 2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 5, 1, 1, 6, 4]
    solution = Solution()
    print(f"Example 1: nums before wiggle sort = {nums1}")
    solution.wiggleSort(nums1)
    print(f"Output after wiggle sort: {nums1}")
    print("-" * 20)

    # Example 2
    nums2 = [1, 3, 2, 2, 3, 1]
    print(f"Example 2: nums before wiggle sort = {nums2}")
    solution.wiggleSort(nums2)
    print(f"Output after wiggle sort: {nums2}")
    print("-" * 20)

    # Example 3
    nums3 = [1, 1, 2, 1, 2, 2, 1]
    print(f"Example 3: nums before wiggle sort = {nums3}")
    solution.wiggleSort(nums3)
    print(f"Output after wiggle sort: {nums3}")
    print("-" * 20)

    # Example 4 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., 1 5 1 1 6 4): ")
        user_nums = list(map(int, user_nums_str.split()))
        
        print(f"User Input before wiggle sort: {user_nums}")
        solution.wiggleSort(user_nums)
        print(f"Output after wiggle sort: {user_nums}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")