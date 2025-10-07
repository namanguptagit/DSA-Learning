from typing import List

class Solution:
    def findLengthOfLCIS(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 1
        l = 1 
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                l += 1
                longest = max(longest, l)
            else:
                l = 1
        return longest

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    arr1 = [1, 3, 5, 4, 7]
    solution = Solution()
    result1 = solution.findLengthOfLCIS(arr1)
    print(f"Example 1: arr = {arr1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    arr2 = [2, 2, 2, 2, 2]
    result2 = solution.findLengthOfLCIS(arr2)
    print(f"Example 2: arr = {arr2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    arr3 = [1, 3, 5, 7]
    result3 = solution.findLengthOfLCIS(arr3)
    print(f"Example 3: arr = {arr3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4
    arr4 = [7, 5, 3, 1]
    result4 = solution.findLengthOfLCIS(arr4)
    print(f"Example 4: arr = {arr4}")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_arr_str = input("Enter a list of numbers separated by spaces (e.g., 1 3 5 4 7): ")
        user_arr = list(map(int, user_arr_str.split()))

        user_result = solution.findLengthOfLCIS(user_arr)
        print(f"User Input: arr = {user_arr}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")