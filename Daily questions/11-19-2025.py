class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        seen = set(nums)
        x = original
        while x <= 1000:
            if x in seen:
                x *= 2
            else:
                break
        return x

# Simple tests consistent with repository style (print + assert)
def test_findFinalValue():
    solver = Solution()

    # Test 1: Example where original is doubled several times
    nums1 = [5,3,6,1,12]
    original1 = 3
    expected1 = 24
    out1 = solver.findFinalValue(nums1, original1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: original not present; should return original
    nums2 = [1,2,4,8,16]
    original2 = 5
    expected2 = 5
    out2 = solver.findFinalValue(nums2, original2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: original in nums, but not next double
    nums3 = [2,7,3]
    original3 = 3
    expected3 = 6
    out3 = solver.findFinalValue(nums3, original3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: All powers of 2 to 16, start with 1
    nums4 = [1,2,4,8,16,32]
    original4 = 1
    expected4 = 64
    out4 = solver.findFinalValue(nums4, original4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Large original not present
    nums5 = [2,4,8]
    original5 = 100
    expected5 = 100
    out5 = solver.findFinalValue(nums5, original5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Duplicates in nums
    nums6 = [2,2,2,4,8,8]
    original6 = 2
    expected6 = 16
    out6 = solver.findFinalValue(nums6, original6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Edge test: Empty nums
    nums7 = []
    original7 = 42
    expected7 = 42
    out7 = solver.findFinalValue(nums7, original7)
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for findFinalValue.")

if __name__ == "__main__":
    test_findFinalValue()