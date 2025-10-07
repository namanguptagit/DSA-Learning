from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 0
        
        for i in range(1, n-1):
            # check if arr[i] is a peak
            if arr[i-1] < arr[i] > arr[i+1]:
                l, r = i, i
                # expand left
                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1
                # expand right
                while r < n-1 and arr[r] > arr[r+1]:
                    r += 1
                # update max
                longest = max(longest, r - l + 1)
        
        return longest

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    arr1 = [2, 1, 4, 7, 3, 2, 5]
    solution = Solution()
    result1 = solution.longestMountain(arr1)
    print(f"Example 1: arr = {arr1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    arr2 = [2, 2, 2]
    result2 = solution.longestMountain(arr2)
    print(f"Example 2: arr = {arr2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    arr3 = [1, 2, 3, 4, 5]
    result3 = solution.longestMountain(arr3)
    print(f"Example 3: arr = {arr3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4
    arr4 = [5, 4, 3, 2, 1]
    result4 = solution.longestMountain(arr4)
    print(f"Example 4: arr = {arr4}")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_arr_str = input("Enter a list of numbers separated by spaces (e.g., 2 1 4 7 3 2 5): ")
        user_arr = list(map(int, user_arr_str.split()))

        user_result = solution.longestMountain(user_arr)
        print(f"User Input: arr = {user_arr}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")