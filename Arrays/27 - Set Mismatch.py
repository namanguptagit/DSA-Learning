from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        duplicate = sum(nums) - sum(num_set)
        missing = int(n*(n+1)/2) - sum(num_set)
        return [duplicate,missing]


# Simple tests consistent with repository style (print + assert)
def test_findErrorNums():
    solver = Solution()

    # Test 1: Basic example
    nums1 = [1, 2, 2, 4]
    res1 = solver.findErrorNums(nums1)
    print("Test 1:", nums1, "->", res1)
    assert res1 == [2, 3]  # duplicate: 2, missing: 3

    # Test 2: Duplicate at the beginning
    nums2 = [2, 2]
    res2 = solver.findErrorNums(nums2)
    print("Test 2:", nums2, "->", res2)
    assert res2 == [2, 1]  # duplicate: 2, missing: 1

    # Test 3: Duplicate at the end
    nums3 = [1, 1]
    res3 = solver.findErrorNums(nums3)
    print("Test 3:", nums3, "->", res3)
    assert res3 == [1, 2]  # duplicate: 1, missing: 2

    # Test 4: Larger array
    nums4 = [1, 2, 3, 4, 4, 6]
    res4 = solver.findErrorNums(nums4)
    print("Test 4:", nums4, "->", res4)
    assert res4 == [4, 5]  # duplicate: 4, missing: 5

    # Test 5: Missing number is 1 (different array)
    nums5 = [3, 2, 2]
    res5 = solver.findErrorNums(nums5)
    print("Test 5:", nums5, "->", res5)
    assert res5 == [2, 1]  # duplicate: 2, missing: 1

    # Test 6: Missing number is at the end
    nums6 = [1, 2, 2]
    res6 = solver.findErrorNums(nums6)
    print("Test 6:", nums6, "->", res6)
    assert res6 == [2, 3]  # duplicate: 2, missing: 3

    # Test 7: Duplicate in the middle
    nums7 = [1, 3, 3, 4]
    res7 = solver.findErrorNums(nums7)
    print("Test 7:", nums7, "->", res7)
    assert res7 == [3, 2]  # duplicate: 3, missing: 2

    # Test 8: Another example
    nums8 = [3, 2, 3, 4, 6, 5]
    res8 = solver.findErrorNums(nums8)
    print("Test 8:", nums8, "->", res8)
    assert res8 == [3, 1]  # duplicate: 3, missing: 1

    # Test 9: Larger array with duplicate
    nums9 = [1, 5, 3, 2, 2, 7, 4, 6, 8, 9]
    res9 = solver.findErrorNums(nums9)
    print("Test 9:", nums9, "->", res9)
    assert res9 == [2, 10]  # duplicate: 2, missing: 10

    # Test 10: Single element (edge case - n=1)
    nums10 = [1, 1]
    res10 = solver.findErrorNums(nums10)
    print("Test 10:", nums10, "->", res10)
    assert res10 == [1, 2]  # duplicate: 1, missing: 2

    print("All tests passed!")


if __name__ == "__main__":
    test_findErrorNums()