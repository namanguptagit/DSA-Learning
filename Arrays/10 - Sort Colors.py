from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        x,y,z = 0,0,n-1
        while(y<=z):
            if nums[y] == 0:
                nums[x], nums[y] = nums[y], nums[x]
                x+=1
                y+=1
            elif nums[y] == 1:
                y+=1
            elif nums[y] == 2:
                nums[y], nums[z] = nums[z], nums[y]
                z-=1

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    nums1 = [2, 0, 2, 1, 1, 0]
    solution = Solution()
    print(f"Example 1: nums before sorting = {nums1}")
    solution.sortColors(nums1)
    print(f"Output after sorting: {nums1}")
    print("-" * 20)

    # Example 2
    nums2 = [2, 0, 1]
    print(f"Example 2: nums before sorting = {nums2}")
    solution.sortColors(nums2)
    print(f"Output after sorting: {nums2}")
    print("-" * 20)

    # Example 3
    nums3 = [0]
    print(f"Example 3: nums before sorting = {nums3}")
    solution.sortColors(nums3)
    print(f"Output after sorting: {nums3}")
    print("-" * 20)

    # Example 4 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers (0, 1, 2) separated by spaces (e.g., 2 0 2 1 1 0): ")
        user_nums = list(map(int, user_nums_str.split()))
        
        # Validate input
        if not all(x in [0, 1, 2] for x in user_nums):
            print("Invalid input. Please enter only 0, 1, and 2.")
        else:
            print(f"User Input before sorting: {user_nums}")
            solution.sortColors(user_nums)
            print(f"Output after sorting: {user_nums}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
