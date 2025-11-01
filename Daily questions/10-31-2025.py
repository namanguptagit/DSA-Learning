from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [False] * n
        res = []
        for num in nums:
            if seen[num]:
                res.append(num)
            else:
                seen[num] = True
        return res


# Simple tests consistent with repository style (print + assert)
def test_getSneakyNumbers():
    solver = Solution()

    # Test 1: Single element (no duplicates)
    nums1 = [0]
    res1 = solver.getSneakyNumbers(nums1)
    print("Test 1:", nums1, "->", res1)
    assert res1 == []

    # Test 2: Two elements, one duplicate
    nums2 = [0, 0]
    res2 = solver.getSneakyNumbers(nums2)
    print("Test 2:", nums2, "->", res2)
    assert res2 == [0]

    # Test 3: Multiple duplicates
    nums3 = [1, 1, 2, 2, 3]
    res3 = solver.getSneakyNumbers(nums3)
    print("Test 3:", nums3, "->", res3)
    assert res3 == [1, 2]

    # Test 4: No duplicates
    nums4 = [0, 1, 2, 3]
    res4 = solver.getSneakyNumbers(nums4)
    print("Test 4:", nums4, "->", res4)
    assert res4 == []

    # Test 5: All duplicates
    nums5 = [0, 0, 0, 0]
    res5 = solver.getSneakyNumbers(nums5)
    print("Test 5:", nums5, "->", res5)
    assert res5 == [0, 0, 0]

    # Test 6: Mixed pattern
    nums6 = [1, 0, 2, 1, 0, 3]
    res6 = solver.getSneakyNumbers(nums6)
    print("Test 6:", nums6, "->", res6)
    assert res6 == [1, 0]

    # Test 7: Empty array
    nums7 = []
    res7 = solver.getSneakyNumbers(nums7)
    print("Test 7:", nums7, "->", res7)
    assert res7 == []

    # Test 8: Sequential duplicates
    nums8 = [0, 1, 2, 0, 1, 2]
    res8 = solver.getSneakyNumbers(nums8)
    print("Test 8:", nums8, "->", res8)
    assert res8 == [0, 1, 2]

    # Test 9: Non-sequential duplicates
    nums9 = [3, 1, 2, 3, 1, 4]
    res9 = solver.getSneakyNumbers(nums9)
    print("Test 9:", nums9, "->", res9)
    assert res9 == [3, 1]

    # Test 10: Multiple occurrences of same number
    nums10 = [2, 2, 2, 2, 2]
    res10 = solver.getSneakyNumbers(nums10)
    print("Test 10:", nums10, "->", res10)
    assert res10 == [2, 2, 2, 2]

    # Test 11: Single duplicate at end
    nums11 = [0, 1, 2, 3, 2]
    res11 = solver.getSneakyNumbers(nums11)
    print("Test 11:", nums11, "->", res11)
    assert res11 == [2]

    # Test 12: Duplicate at beginning
    nums12 = [1, 1, 2, 3, 4]
    res12 = solver.getSneakyNumbers(nums12)
    print("Test 12:", nums12, "->", res12)
    assert res12 == [1]

    print("All tests passed!")


if __name__ == "__main__":
    test_getSneakyNumbers()