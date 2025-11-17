class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        prev = None
        for i, num in enumerate(nums):
            if num == 1:
                if prev is not None and i - prev <= k:
                    return False
                prev = i
        return True

# Simple tests consistent with repository style (print + assert)
def test_kLengthApart():
    solver = Solution()
    
    # Test 1: Basic example, should return True
    nums1 = [1,0,0,0,1,0,0,1]
    k1 = 2
    expected1 = True
    out1 = solver.kLengthApart(nums1, k1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Close ones violating k
    nums2 = [1,0,1,0,1]
    k2 = 2
    expected2 = False
    out2 = solver.kLengthApart(nums2, k2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: All zeros
    nums3 = [0,0,0,0]
    k3 = 1
    expected3 = True
    out3 = solver.kLengthApart(nums3, k3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: k = 0 (all ones allowed together)
    nums4 = [1,1,1,1,0,0,1]
    k4 = 0
    expected4 = True
    out4 = solver.kLengthApart(nums4, k4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Single 1
    nums5 = [0,0,1,0,0]
    k5 = 3
    expected5 = True
    out5 = solver.kLengthApart(nums5, k5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Edge - first and last ones too close
    nums6 = [1,0,0,1]
    k6 = 3
    expected6 = True
    out6 = solver.kLengthApart(nums6, k6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Edge - exactly k apart
    nums7 = [1,0,0,0,1]
    k7 = 3
    expected7 = True
    out7 = solver.kLengthApart(nums7, k7)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: Not enough separation
    nums8 = [1,0,0,1]
    k8 = 2
    expected8 = True
    out8 = solver.kLengthApart(nums8, k8)
    print("Test 8:", out8)
    assert out8 == expected8

    # Test 9: Violation
    nums9 = [1,1]
    k9 = 1
    expected9 = False
    out9 = solver.kLengthApart(nums9, k9)
    print("Test 9:", out9)
    assert out9 == expected9

    print("All tests passed for kLengthApart.")

if __name__ == "__main__":
    test_kLengthApart()