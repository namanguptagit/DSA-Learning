class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        for i in range(len(nums)):
            val = ((val << 1) + nums[i]) % 5
            nums[i] = val == 0
        return nums

# Test cases
if __name__ == "__main__":
    sol = Solution()
    # Test case 1
    print(sol.prefixesDivBy5([0,1,1])) # [True, False, False]
    # Test case 2
    print(sol.prefixesDivBy5([1,1,1,0,1])) # [False, False, False, False, True]
    # Test case 3
    print(sol.prefixesDivBy5([0,0,0])) # [True, True, True]
    # Test case 4
    print(sol.prefixesDivBy5([1,0,1,1,1,1])) # [False, False, False, True, False, False]