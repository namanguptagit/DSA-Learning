class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeros, res = 0, 0, 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            res = max(res, right - left)
        
        return res

# Simple tests consistent with repository style (print + assert)
def test_longestSubarray():
    solver = Solution()

    # Test 1: Example from Leetcode
    nums1 = [1,1,0,1]
    expected1 = 3
    out1 = solver.longestSubarray(nums1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Only zeros
    nums2 = [0,0,0]
    expected2 = 0
    out2 = solver.longestSubarray(nums2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: All ones
    nums3 = [1,1,1,1]
    expected3 = 3 # need to "delete one element", so one less than total
    out3 = solver.longestSubarray(nums3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: 1 zero between ones
    nums4 = [1,1,0,1,1,1]
    expected4 = 5
    out4 = solver.longestSubarray(nums4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Zero at the end
    nums5 = [1,1,1,0]
    expected5 = 3
    out5 = solver.longestSubarray(nums5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Zero at the beginning
    nums6 = [0,1,1,1]
    expected6 = 3
    out6 = solver.longestSubarray(nums6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Alternating ones and zeros
    nums7 = [1,0,1,0,1,0,1]
    expected7 = 2
    out7 = solver.longestSubarray(nums7)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: Single zero in the middle of longer array
    nums8 = [1,1,1,0,1,1]
    expected8 = 5
    out8 = solver.longestSubarray(nums8)
    print("Test 8:", out8)
    assert out8 == expected8

    # Test 9: Single element [1]
    nums9 = [1]
    expected9 = 0
    out9 = solver.longestSubarray(nums9)
    print("Test 9:", out9)
    assert out9 == expected9

    # Test 10: Single element [0]
    nums10 = [0]
    expected10 = 0
    out10 = solver.longestSubarray(nums10)
    print("Test 10:", out10)
    assert out10 == expected10

    print("All tests passed for longestSubarray.")

if __name__ == "__main__":
    test_longestSubarray()