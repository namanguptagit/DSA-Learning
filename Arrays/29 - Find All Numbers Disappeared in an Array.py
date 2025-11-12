from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1  # mark as seen
        
        # positive values → missing numbers
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# Simple tests consistent with repository style (print + assert)
def test_findDisappearedNumbers():
    solver = Solution()

    # Test 1: Basic example
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    res1 = solver.findDisappearedNumbers(nums1)
    print("Test 1:", nums1, "->", res1)
    assert sorted(res1) == [5, 6]  # Missing: 5, 6

    # Test 2: Single missing number
    nums2 = [1, 1]
    res2 = solver.findDisappearedNumbers(nums2)
    print("Test 2:", nums2, "->", res2)
    assert sorted(res2) == [2]  # Missing: 2

    # Test 3: All numbers present
    nums3 = [1, 2, 3, 4]
    res3 = solver.findDisappearedNumbers(nums3)
    print("Test 3:", nums3, "->", res3)
    assert sorted(res3) == []  # No missing numbers

    # Test 4: Multiple missing numbers
    nums4 = [1, 1, 1, 1]
    res4 = solver.findDisappearedNumbers(nums4)
    print("Test 4:", nums4, "->", res4)
    assert sorted(res4) == [2, 3, 4]  # Missing: 2, 3, 4

    # Test 5: Missing at the beginning
    nums5 = [2, 2]
    res5 = solver.findDisappearedNumbers(nums5)
    print("Test 5:", nums5, "->", res5)
    assert sorted(res5) == [1]  # Missing: 1

    # Test 6: Missing at the end
    nums6 = [1, 2, 3, 3]
    res6 = solver.findDisappearedNumbers(nums6)
    print("Test 6:", nums6, "->", res6)
    assert sorted(res6) == [4]  # Missing: 4

    # Test 7: Larger array
    nums7 = [1, 1, 2, 2, 3, 3, 4, 4]
    res7 = solver.findDisappearedNumbers(nums7)
    print("Test 7:", nums7, "->", res7)
    assert sorted(res7) == [5, 6, 7, 8]  # Missing: 5, 6, 7, 8

    # Test 8: Scattered missing numbers
    nums8 = [2, 4, 4, 2]
    res8 = solver.findDisappearedNumbers(nums8)
    print("Test 8:", nums8, "->", res8)
    assert sorted(res8) == [1, 3]  # Missing: 1, 3

    # Test 9: Single element array
    nums9 = [1]
    res9 = solver.findDisappearedNumbers(nums9)
    print("Test 9:", nums9, "->", res9)
    assert sorted(res9) == []  # No missing numbers

    # Test 10: All duplicates
    nums10 = [3, 3, 3, 3]
    res10 = solver.findDisappearedNumbers(nums10)
    print("Test 10:", nums10, "->", res10)
    assert sorted(res10) == [1, 2, 4]  # Missing: 1, 2, 4

    print("All tests passed!")


if __name__ == "__main__":
    test_findDisappearedNumbers()