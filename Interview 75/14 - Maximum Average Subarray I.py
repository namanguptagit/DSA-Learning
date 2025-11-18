class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)
        return maxSum / k

# Simple tests consistent with repository style (print + assert)
def test_findMaxAverage():
    solver = Solution()

    # Test 1: Example from Leetcode
    nums1 = [1,12,-5,-6,50,3]
    k1 = 4
    expected1 = 12.75
    out1 = solver.findMaxAverage(nums1, k1)
    print("Test 1:", out1)
    assert abs(out1 - expected1) < 1e-5

    # Test 2: All elements equal
    nums2 = [5,5,5,5,5]
    k2 = 1
    expected2 = 5.0
    out2 = solver.findMaxAverage(nums2, k2)
    print("Test 2:", out2)
    assert abs(out2 - expected2) < 1e-5

    # Test 3: k equals length of nums
    nums3 = [0,4,0,3,2]
    k3 = 5
    expected3 = (0+4+0+3+2)/5
    out3 = solver.findMaxAverage(nums3, k3)
    print("Test 3:", out3)
    assert abs(out3 - expected3) < 1e-5

    # Test 4: Negative numbers
    nums4 = [-1,-12,-5,-6,-50,-3]
    k4 = 2
    expected4 = max([-1-12, -12-5, -5-6, -6-50, -50-3])/2
    out4 = solver.findMaxAverage(nums4, k4)
    print("Test 4:", out4)
    # Let's compute expected4 precisely:
    possible = [[nums4[i], nums4[i+1]] for i in range(len(nums4)-1)]
    expected4 = max([sum(x) for x in possible])/2
    assert abs(out4 - expected4) < 1e-5

    # Test 5: k = len(nums) - 1
    nums5 = [1,2,3,4]
    k5 = 3
    expected5 = max(sum(nums5[i:i+3]) for i in range(2)) / 3
    out5 = solver.findMaxAverage(nums5, k5)
    print("Test 5:", out5)
    assert abs(out5 - expected5) < 1e-5

    print("All tests passed for findMaxAverage.")

if __name__ == "__main__":
    test_findMaxAverage()