from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = 0
        for i in range (m,m+n):
            nums1[i] = nums2[k]
            k+=1
        nums1.sort()

# Another Approach Better Time Complexity
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1    
        j = n - 1       
        k = m + n - 1 
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1 - First Approach
    nums1_1 = [1, 2, 3, 0, 0, 0]
    m1 = 3
    nums2_1 = [2, 5, 6]
    n1 = 3
    solution1 = Solution()
    print(f"Example 1 (First Approach): nums1 = {nums1_1}, m = {m1}, nums2 = {nums2_1}, n = {n1}")
    solution1.merge(nums1_1, m1, nums2_1, n1)
    print(f"Output: {nums1_1}")
    print("-" * 20)

    # Example 2 - First Approach
    nums1_2 = [1]
    m2 = 1
    nums2_2 = []
    n2 = 0
    print(f"Example 2 (First Approach): nums1 = {nums1_2}, m = {m2}, nums2 = {nums2_2}, n = {n2}")
    solution1.merge(nums1_2, m2, nums2_2, n2)
    print(f"Output: {nums1_2}")
    print("-" * 20)

    # Example 1 - Second Approach (Better Time Complexity)
    nums1_3 = [1, 2, 3, 0, 0, 0]
    m3 = 3
    nums2_3 = [2, 5, 6]
    n3 = 3
    solution2 = Solution()
    print(f"Example 1 (Second Approach): nums1 = {nums1_3}, m = {m3}, nums2 = {nums2_3}, n = {n3}")
    solution2.merge(nums1_3, m3, nums2_3, n3)
    print(f"Output: {nums1_3}")
    print("-" * 20)

    # Example 2 - Second Approach (Better Time Complexity)
    nums1_4 = [0]
    m4 = 0
    nums2_4 = [1]
    n4 = 1
    print(f"Example 2 (Second Approach): nums1 = {nums1_4}, m = {m4}, nums2 = {nums2_4}, n = {n4}")
    solution2.merge(nums1_4, m4, nums2_4, n4)
    print(f"Output: {nums1_4}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take nums1 input
        nums1_str = input("Enter nums1 array (format: 1 2 3 0 0 0): ").split()
        nums1 = list(map(int, nums1_str))
        
        # Take m input
        m = int(input("Enter m (number of elements in nums1): "))
        
        # Take nums2 input
        nums2_str = input("Enter nums2 array (format: 2 5 6): ").split()
        nums2 = list(map(int, nums2_str))
        
        # Take n input
        n = int(input("Enter n (number of elements in nums2): "))

        print(f"User Input: nums1 = {nums1}, m = {m}, nums2 = {nums2}, n = {n}")
        solution2.merge(nums1, m, nums2, n)
        print(f"Output: {nums1}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")