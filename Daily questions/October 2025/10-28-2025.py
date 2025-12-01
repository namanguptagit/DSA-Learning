from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
            right[n - i - 1] = right[n - i] + nums[n - i]

        for i in range(n):
            if nums[i] != 0:
                continue
            if left[i] == right[i]:
                count += 2
            elif abs(left[i] - right[i]) == 1:
                count += 1

        return count


# Simple tests consistent with repository style (print + assert)
def test_countValidSelections():
    solver = Solution()

    # Test 1: Empty array
    nums1 = []
    res1 = solver.countValidSelections(nums1)
    print("Test 1:", nums1, "->", res1)
    assert res1 == 0

    # Test 2: No zeros
    nums2 = [1, 2, 3]
    res2 = solver.countValidSelections(nums2)
    print("Test 2:", nums2, "->", res2)
    assert res2 == 0

    # Test 3: Single zero with equal sums
    nums3 = [1, 0, 1]
    res3 = solver.countValidSelections(nums3)
    print("Test 3:", nums3, "->", res3)
    assert res3 == 2

    # Test 4: Single zero with difference of 1
    nums4 = [1, 0, 2]
    res4 = solver.countValidSelections(nums4)
    print("Test 4:", nums4, "->", res4)
    assert res4 == 1

    # Test 5: Multiple zeros
    nums5 = [1, 0, 1, 0, 1]
    res5 = solver.countValidSelections(nums5)
    print("Test 5:", nums5, "->", res5)
    assert res5 == 4

    # Test 6: Zero at start
    nums6 = [0, 1, 1]
    res6 = solver.countValidSelections(nums6)
    print("Test 6:", nums6, "->", res6)
    assert res6 == 1

    # Test 7: Zero at end
    nums7 = [1, 1, 0]
    res7 = solver.countValidSelections(nums7)
    print("Test 7:", nums7, "->", res7)
    assert res7 == 1

    # Test 8: All zeros
    nums8 = [0, 0, 0]
    res8 = solver.countValidSelections(nums8)
    print("Test 8:", nums8, "->", res8)
    assert res8 == 6

    # Test 9: Mixed case with large difference
    nums9 = [5, 0, 1]
    res9 = solver.countValidSelections(nums9)
    print("Test 9:", nums9, "->", res9)
    assert res9 == 0

    # Test 10: Complex case
    nums10 = [2, 0, 1, 0, 1, 2]
    res10 = solver.countValidSelections(nums10)
    print("Test 10:", nums10, "->", res10)
    assert res10 == 4

    print("All tests passed!")


if __name__ == "__main__":
    test_countValidSelections()