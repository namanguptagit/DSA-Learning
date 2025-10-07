from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        j , k = 0 , n-1
        pos = n-1
        while (j <= k):
            if abs(nums[j]) > abs(nums[k]):
                res[pos] = nums[j]*nums[j]
                j+=1
            else:
                res[pos] = nums[k]*nums[k]
                k-=1
            pos-=1
        return res

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    nums1 = [-4, -1, 0, 3, 10]
    solution = Solution()
    result1 = solution.sortedSquares(nums1)
    print(f"Example 1: nums = {nums1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    nums2 = [-7, -3, 2, 3, 11]
    result2 = solution.sortedSquares(nums2)
    print(f"Example 2: nums = {nums2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a sorted list of numbers separated by spaces (e.g., -4 -1 0 3 10): ")
        user_nums = list(map(int, user_nums_str.split()))

        user_result = solution.sortedSquares(user_nums)
        print(f"User Input: nums = {user_nums}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")