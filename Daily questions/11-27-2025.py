class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefSum = 0
        subMax = -sys.maxsize
        minSoFar = [sys.maxsize] * k
        minSoFar[(k - 1) % k] = 0

        for i, v in enumerate(nums):
            prefSum += v
            subMax = max(subMax, prefSum - minSoFar[i % k])
            minSoFar[i % k] = min(minSoFar[i % k], prefSum)

        return subMax

# Simple tests consistent with repository style (print + assert)
def test_maxSubarraySum():
    solver = Solution()
    
    # Test 1: Basic example, nums divisible by k
    nums1 = [2, 3, 1, 4, 5]
    k1 = 3
    out1 = solver.maxSubarraySum(nums1, k1)
    print("Test 1:", out1)
    assert out1 == 15  # Whole array, sum 15, 15 % 3 == 0

    # Test 2: No subarray divisible by k
    nums2 = [1, 2, 5]
    k2 = 4
    out2 = solver.maxSubarraySum(nums2, k2)
    print("Test 2:", out2)
    assert out2 == 0  # Subarray [1,2,5]=8, not divisible, but [0] (empty is not valid), so answer is 0 (if required to be non-empty, else -sys.maxsize)

    # Test 3: Minimum element, negatives
    nums3 = [-1, -2, -3]
    k3 = 2
    out3 = solver.maxSubarraySum(nums3, k3)
    print("Test 3:", out3)
    assert out3 == -2  # subarray [-2] (sum -2), -2%2==0

    # Test 4: Single element matching k
    nums4 = [7]
    k4 = 7
    out4 = solver.maxSubarraySum(nums4, k4)
    print("Test 4:", out4)
    assert out4 == 7

    # Test 5: Subarray not at start
    nums5 = [1, 2, 3, 4, 5]
    k5 = 6
    out5 = solver.maxSubarraySum(nums5, k5)
    print("Test 5:", out5)
    assert out5 == 6  # [1,2,3] = 6

    # Test 6: All zeros
    nums6 = [0, 0, 0]
    k6 = 1
    out6 = solver.maxSubarraySum(nums6, k6)
    print("Test 6:", out6)
    assert out6 == 0

if __name__ == "__main__":
    test_maxSubarraySum()