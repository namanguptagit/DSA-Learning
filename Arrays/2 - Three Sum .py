from typing import List

# Trying Brute Force Approach first
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        my_set = set()
        for i in range (0,n):
            for j in range (i+1,n):
                for k in range (j+1,n):
                    if(nums[i]+nums[j]+nums[k] == 0):
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        my_set.add(tuple(temp))
        return [list(ans) for ans in my_set ]
# Time Complexity: O(n^3)
#A Better Approach will try to do it in O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        my_set = set()
        for i in range (0,n):
            check_set = set()
            for j in range (i+1,n):
                third = -(nums[i]+nums[j])
                if(third in check_set):
                    temp=[nums[i],nums[j],third]
                    temp.sort()
                    my_set.add(tuple(temp))
                check_set.add(nums[j])
        return [list(ans) for ans in my_set]

# Now a Better Approach 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range (n):
            if (i!=0 and nums[i] == nums[i-1]):
                continue
            j = i+1
            k = n-1
            while(j<k):
                total_sum = nums[i] +nums[j] +nums[k]
                if total_sum<0 :
                    j+=1
                elif total_sum>0 :
                    k-=1
                else : 
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return ans

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result1 = solution.threeSum(nums1)
    print(f"Example 1: nums = {nums1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    print(f"Example 2: nums = {nums2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    print(f"Example 3: nums = {nums3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., -1 0 1 2 -1 -4): ")
        user_nums = list(map(int, user_nums_str.split()))

        user_result = solution.threeSum(user_nums)
        print(f"User Input: nums = {user_nums}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")        