class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return idx      
            leftSum += ele
        return -1 

# Simple tests consistent with repository style (print + assert)
def test_pivotIndex():
    solver = Solution()

    # Test 1: Example with unique pivot
    nums1 = [1, 7, 3, 6, 5, 6]
    expected1 = 3
    out1 = solver.pivotIndex(nums1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Example with pivot at 0
    nums2 = [2, 1, -1]
    expected2 = 0
    out2 = solver.pivotIndex(nums2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: No pivot exists
    nums3 = [1, 2, 3]
    expected3 = -1
    out3 = solver.pivotIndex(nums3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Empty array
    nums4 = []
    expected4 = -1
    out4 = solver.pivotIndex(nums4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: All zeros (all indices are pivots, should return 0)
    nums5 = [0, 0, 0, 0]
    expected5 = 0
    out5 = solver.pivotIndex(nums5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Single element (should return 0)
    nums6 = [8]
    expected6 = 0
    out6 = solver.pivotIndex(nums6)
    print("Test 6:", out6)
    assert out6 == expected6

    print("All tests passed for pivotIndex.")

if __name__ == "__main__":
    test_pivotIndex()