class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] % 3 != 0:
                count += 1
        return count

# Simple tests consistent with repository style (print + assert)
def test_minimumOperations():
    solver = Solution()

    # Test 1: Typical input with various mods
    nums1 = [3, 6, 7, 4, 5]
    expected1 = 3  # 7, 4, 5 are not divisible by 3
    out1 = solver.minimumOperations(nums1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: All divisible by 3
    nums2 = [3, 6, 9, 12]
    expected2 = 0
    out2 = solver.minimumOperations(nums2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: None divisible by 3
    nums3 = [1, 2, 4, 5, 7, 8]
    expected3 = 6
    out3 = solver.minimumOperations(nums3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Empty list
    nums4 = []
    expected4 = 0
    out4 = solver.minimumOperations(nums4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Single element divisible by 3
    nums5 = [9]
    expected5 = 0
    out5 = solver.minimumOperations(nums5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Single element not divisible by 3
    nums6 = [10]
    expected6 = 1
    out6 = solver.minimumOperations(nums6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Negative numbers
    nums7 = [-3, -6, -8, -2]
    expected7 = 2  # -8, -2 are not divisible by 3
    out7 = solver.minimumOperations(nums7)
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for minimumOperations.")

if __name__ == "__main__":
    test_minimumOperations()