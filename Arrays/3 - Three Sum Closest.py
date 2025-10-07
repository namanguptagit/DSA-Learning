from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        ans = 9999999999999999
        nums.sort()
        for i in range(n):
            if(i!=0 and nums[i] == nums[i-1]):
                continue
            j=i+1
            k=n-1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if abs(target - total_sum) < abs(target - ans):
                    ans = total_sum
                if total_sum < target:
                    j += 1
                elif total_sum > target:
                    k -= 1
                else:
                    return target
        return ans

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    solution = Solution()
    result1 = solution.threeSumClosest(nums1, target1)
    print(f"Example 1: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    nums2 = [0, 0, 0]
    target2 = 1
    result2 = solution.threeSumClosest(nums2, target2)
    print(f"Example 2: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_nums_str = input("Enter a list of numbers separated by spaces (e.g., -1 2 1 -4): ")
        user_nums = list(map(int, user_nums_str.split()))

        # Take target input
        user_target = int(input("Enter the target number: "))

        user_result = solution.threeSumClosest(user_nums, user_target)
        print(f"User Input: nums = {user_nums}, target = {user_target}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")