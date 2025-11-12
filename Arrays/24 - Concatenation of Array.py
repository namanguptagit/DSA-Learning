from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * (len(nums)*2)
        for i in range(0,len(nums)):
            ans[i]=nums[i]
            ans[i+len(nums)]=nums[i]
        return ans


# Simple tests consistent with repository style (print + assert)
def test_getConcatenation():
    solver = Solution()

    # Test 1: Basic example
    nums1 = [1, 2, 1]
    res1 = solver.getConcatenation(nums1)
    print("Test 1:", nums1, "->", res1)
    assert res1 == [1, 2, 1, 1, 2, 1]

    # Test 2: Single element
    nums2 = [1]
    res2 = solver.getConcatenation(nums2)
    print("Test 2:", nums2, "->", res2)
    assert res2 == [1, 1]

    # Test 3: Two elements
    nums3 = [1, 3]
    res3 = solver.getConcatenation(nums3)
    print("Test 3:", nums3, "->", res3)
    assert res3 == [1, 3, 1, 3]

    # Test 4: Multiple elements
    nums4 = [1, 2, 3, 4]
    res4 = solver.getConcatenation(nums4)
    print("Test 4:", nums4, "->", res4)
    assert res4 == [1, 2, 3, 4, 1, 2, 3, 4]

    # Test 5: Array with zeros
    nums5 = [0, 1, 0]
    res5 = solver.getConcatenation(nums5)
    print("Test 5:", nums5, "->", res5)
    assert res5 == [0, 1, 0, 0, 1, 0]

    # Test 6: Array with negative numbers
    nums6 = [-1, -2, -3]
    res6 = solver.getConcatenation(nums6)
    print("Test 6:", nums6, "->", res6)
    assert res6 == [-1, -2, -3, -1, -2, -3]

    # Test 7: Array with duplicates
    nums7 = [5, 5, 5]
    res7 = solver.getConcatenation(nums7)
    print("Test 7:", nums7, "->", res7)
    assert res7 == [5, 5, 5, 5, 5, 5]

    # Test 8: Larger array
    nums8 = [1, 2, 3, 4, 5, 6]
    res8 = solver.getConcatenation(nums8)
    print("Test 8:", nums8, "->", res8)
    assert res8 == [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

    print("All tests passed!")


if __name__ == "__main__":
    test_getConcatenation()