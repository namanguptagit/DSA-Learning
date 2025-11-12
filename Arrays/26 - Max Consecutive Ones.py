from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                count = 0
            ans = max(ans,count)
        return ans


# Simple tests consistent with repository style (print + assert)
def test_findMaxConsecutiveOnes():
    solver = Solution()

    # Test 1: Basic example
    nums1 = [1, 1, 0, 1, 1, 1]
    res1 = solver.findMaxConsecutiveOnes(nums1)
    print("Test 1:", nums1, "->", res1)
    assert res1 == 3

    # Test 2: All ones
    nums2 = [1, 1, 1, 1]
    res2 = solver.findMaxConsecutiveOnes(nums2)
    print("Test 2:", nums2, "->", res2)
    assert res2 == 4

    # Test 3: All zeros
    nums3 = [0, 0, 0, 0]
    res3 = solver.findMaxConsecutiveOnes(nums3)
    print("Test 3:", nums3, "->", res3)
    assert res3 == 0

    # Test 4: Single one
    nums4 = [1]
    res4 = solver.findMaxConsecutiveOnes(nums4)
    print("Test 4:", nums4, "->", res4)
    assert res4 == 1

    # Test 5: Single zero
    nums5 = [0]
    res5 = solver.findMaxConsecutiveOnes(nums5)
    print("Test 5:", nums5, "->", res5)
    assert res5 == 0

    # Test 6: Ones at the beginning
    nums6 = [1, 1, 1, 0, 0, 1]
    res6 = solver.findMaxConsecutiveOnes(nums6)
    print("Test 6:", nums6, "->", res6)
    assert res6 == 3

    # Test 7: Ones at the end
    nums7 = [0, 0, 1, 1, 1, 1]
    res7 = solver.findMaxConsecutiveOnes(nums7)
    print("Test 7:", nums7, "->", res7)
    assert res7 == 4

    # Test 8: Alternating pattern
    nums8 = [1, 0, 1, 0, 1, 0, 1]
    res8 = solver.findMaxConsecutiveOnes(nums8)
    print("Test 8:", nums8, "->", res8)
    assert res8 == 1

    # Test 9: Multiple groups of ones
    nums9 = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
    res9 = solver.findMaxConsecutiveOnes(nums9)
    print("Test 9:", nums9, "->", res9)
    assert res9 == 3

    # Test 10: Empty array
    nums10 = []
    res10 = solver.findMaxConsecutiveOnes(nums10)
    print("Test 10:", nums10, "->", res10)
    assert res10 == 0

    # Test 11: Long consecutive sequence
    nums11 = [0, 1, 1, 1, 1, 1, 0, 1, 1]
    res11 = solver.findMaxConsecutiveOnes(nums11)
    print("Test 11:", nums11, "->", res11)
    assert res11 == 5

    print("All tests passed!")


if __name__ == "__main__":
    test_findMaxConsecutiveOnes()