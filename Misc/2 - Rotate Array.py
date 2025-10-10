from typing import List
from math import gcd

class Solution:
    def rotate(self, arr: List[int], d: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        gcdVal = gcd(n, d%n)
        for i in range (gcdVal):
            temp = arr[i]
            j=i
            while True:
                k = (j-d)%n
                if k == i:
                    break
                arr[j] = arr[k]
                j=k
            arr[j] = temp
        return arr

# Add code below this line to test your solution
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    print(f"Example 1: nums = {arr1}, k = {k1}")
    solution.rotate(arr1, k1)
    print(f"Output: {arr1}")
    print("-" * 30)
    
    # Example 2
    arr2 = [-1, -100, 3, 99]
    k2 = 2
    print(f"Example 2: nums = {arr2}, k = {k2}")
    solution.rotate(arr2, k2)
    print(f"Output: {arr2}")
    print("-" * 30)
    
    # Example 3 (single element)
    arr3 = [1]
    k3 = 1
    print(f"Example 3: nums = {arr3}, k = {k3}")
    solution.rotate(arr3, k3)
    print(f"Output: {arr3}")
    print("-" * 30)
    
    # Example 4 (no rotation needed)
    arr4 = [1, 2, 3, 4, 5]
    k4 = 0
    print(f"Example 4: nums = {arr4}, k = {k4}")
    solution.rotate(arr4, k4)
    print(f"Output: {arr4}")
    print("-" * 30)
    
    # Example 5 (k larger than array length)
    arr5 = [1, 2]
    k5 = 5
    print(f"Example 5: nums = {arr5}, k = {k5}")
    solution.rotate(arr5, k5)
    print(f"Output: {arr5}")
    print("-" * 30)
    
    # Example (user input)
    print("Testing with user input...")
    try:
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., 1 2 3 4 5): ")
        user_nums = list(map(int, user_nums_str.split()))
        
        user_k = int(input("Enter the number of steps to rotate: "))
        
        print(f"User Input: nums = {user_nums}, k = {user_k}")
        solution.rotate(user_nums, user_k)
        print(f"Output: {user_nums}")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
