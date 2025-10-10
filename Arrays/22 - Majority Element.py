from typing import List

#Moores Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

# an easy approach 
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

# Add code below this line to test your solution
if __name__ == "__main__":
    solution1 = Solution()  # Moore's Voting Algorithm
    solution2 = Solution2()  # Easy approach
    
    # Example 1
    nums1 = [3, 2, 3]
    result1_moore = solution1.majorityElement(nums1.copy())
    result1_easy = solution2.majorityElement(nums1.copy())
    print(f"Example 1: nums = {nums1}")
    print(f"Moore's Algorithm Output: {result1_moore}")
    print(f"Easy Approach Output: {result1_easy}")
    print("-" * 30)

    # Example 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    result2_moore = solution1.majorityElement(nums2.copy())
    result2_easy = solution2.majorityElement(nums2.copy())
    print(f"Example 2: nums = {nums2}")
    print(f"Moore's Algorithm Output: {result2_moore}")
    print(f"Easy Approach Output: {result2_easy}")
    print("-" * 30)

    # Example 3 - Single element
    nums3 = [1]
    result3_moore = solution1.majorityElement(nums3.copy())
    result3_easy = solution2.majorityElement(nums3.copy())
    print(f"Example 3: nums = {nums3}")
    print(f"Moore's Algorithm Output: {result3_moore}")
    print(f"Easy Approach Output: {result3_easy}")
    print("-" * 30)

    # Example 4 - All same elements
    nums4 = [5, 5, 5, 5]
    result4_moore = solution1.majorityElement(nums4.copy())
    result4_easy = solution2.majorityElement(nums4.copy())
    print(f"Example 4: nums = {nums4}")
    print(f"Moore's Algorithm Output: {result4_moore}")
    print(f"Easy Approach Output: {result4_easy}")
    print("-" * 30)

    # Example 5 - Large array
    nums5 = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
    result5_moore = solution1.majorityElement(nums5.copy())
    result5_easy = solution2.majorityElement(nums5.copy())
    print(f"Example 5: nums = {nums5}")
    print(f"Moore's Algorithm Output: {result5_moore}")
    print(f"Easy Approach Output: {result5_easy}")
    print("-" * 30)

    # Example (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., 3 2 3): ")
        user_nums = list(map(int, user_nums_str.split()))

        user_result_moore = solution1.majorityElement(user_nums.copy())
        user_result_easy = solution2.majorityElement(user_nums.copy())
        print(f"User Input: nums = {user_nums}")
        print(f"Moore's Algorithm Output: {user_result_moore}")
        print(f"Easy Approach Output: {user_result_easy}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")