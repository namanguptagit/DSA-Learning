class Solution:
    def longestOnes(self, nums, k):
        left, maxLength, zeroCount = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength

# Simple tests consistent with repository style (print + assert)
def test_longestOnes():
    solver = Solution()

    # Test 1: Example from Leetcode
    nums1, k1 = [1,1,1,0,0,0,1,1,1,1,0], 2
    expected1 = 6  # Flip two zeros: [1,1,1,0,0,1,1,1,1,1,1] (from idx 5/6)
    out1 = solver.longestOnes(nums1, k1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: All ones
    nums2, k2 = [1,1,1,1], 1
    expected2 = 4
    out2 = solver.longestOnes(nums2, k2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: All zeros, k covers all
    nums3, k3 = [0,0,0,0], 4
    expected3 = 4
    out3 = solver.longestOnes(nums3, k3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Zero k, count max consecutive ones
    nums4, k4 = [1,0,1,1,0,1,1,1,0,0,1], 0
    expected4 = 3
    out4 = solver.longestOnes(nums4, k4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: k exceeds number of zeros
    nums5, k5 = [1,0,1,0,1], 5
    expected5 = 5
    out5 = solver.longestOnes(nums5, k5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Alternating pattern, k=1
    nums6, k6 = [1,0,1,0,1,0,1], 1
    expected6 = 3
    out6 = solver.longestOnes(nums6, k6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Empty array
    nums7, k7 = [], 2
    expected7 = 0
    out7 = solver.longestOnes(nums7, k7)
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for longestOnes.")

if __name__ == "__main__":
    test_longestOnes()