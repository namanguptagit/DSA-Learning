from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        ans = [None] * len(nums)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if j != i:
                    if nums[i] > nums[j]:
                        count+=1
            ans[i] = count
            count = 0
        return ans
# Better Approach
class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        smaller_count = {}
        
        for i, num in enumerate(sorted_nums):
            if num not in smaller_count:
                smaller_count[num] = i  # index = count of smaller numbers
        
        return [smaller_count[num] for num in nums]

# Simple tests consistent with repository style (print + assert)
def test_smallerNumbersThanCurrent():
    solver = Solution()

    # Test 1: Basic example
    nums1 = [8, 1, 2, 2, 3]
    res1 = solver.smallerNumbersThanCurrent(nums1)
    print("Test 1:", nums1, "->", res1)
    assert res1 == [4, 0, 1, 1, 3]

    # Test 2: All same numbers
    nums2 = [7, 7, 7, 7]
    res2 = solver.smallerNumbersThanCurrent(nums2)
    print("Test 2:", nums2, "->", res2)
    assert res2 == [0, 0, 0, 0]

    # Test 3: All different numbers
    nums3 = [6, 5, 4, 8]
    res3 = solver.smallerNumbersThanCurrent(nums3)
    print("Test 3:", nums3, "->", res3)
    assert res3 == [2, 1, 0, 3]

    # Test 4: Single element
    nums4 = [5]
    res4 = solver.smallerNumbersThanCurrent(nums4)
    print("Test 4:", nums4, "->", res4)
    assert res4 == [0]

    # Test 5: Two elements
    nums5 = [1, 2]
    res5 = solver.smallerNumbersThanCurrent(nums5)
    print("Test 5:", nums5, "->", res5)
    assert res5 == [0, 1]

    # Test 6: Sorted array
    nums6 = [1, 2, 3, 4, 5]
    res6 = solver.smallerNumbersThanCurrent(nums6)
    print("Test 6:", nums6, "->", res6)
    assert res6 == [0, 1, 2, 3, 4]

    # Test 7: Reverse sorted array
    nums7 = [5, 4, 3, 2, 1]
    res7 = solver.smallerNumbersThanCurrent(nums7)
    print("Test 7:", nums7, "->", res7)
    assert res7 == [4, 3, 2, 1, 0]

    # Test 8: Array with duplicates
    nums8 = [1, 1, 1, 2, 2, 3]
    res8 = solver.smallerNumbersThanCurrent(nums8)
    print("Test 8:", nums8, "->", res8)
    assert res8 == [0, 0, 0, 3, 3, 5]

    # Test 9: Array with zeros
    nums9 = [0, 1, 2, 3]
    res9 = solver.smallerNumbersThanCurrent(nums9)
    print("Test 9:", nums9, "->", res9)
    assert res9 == [0, 1, 2, 3]

    # Test 10: Array with negative numbers
    nums10 = [-1, 0, 1, 2]
    res10 = solver.smallerNumbersThanCurrent(nums10)
    print("Test 10:", nums10, "->", res10)
    assert res10 == [0, 1, 2, 3]

    # Test 11: Larger array
    nums11 = [5, 0, 10, 0, 10, 6]
    res11 = solver.smallerNumbersThanCurrent(nums11)
    print("Test 11:", nums11, "->", res11)
    assert res11 == [2, 0, 5, 0, 5, 4]

    print("All tests passed!")


if __name__ == "__main__":
    test_smallerNumbersThanCurrent()