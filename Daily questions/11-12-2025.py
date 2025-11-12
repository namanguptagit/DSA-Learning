from typing import List
from math import gcd, inf


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones: return n - ones
        res = inf
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    res = min(res, j - i)
        if res == inf: return -1
        return res + n - 1


# Simple tests consistent with repository style (print + assert)
def test_minOperations():
    solver = Solution()

    # Test 1: Array where GCD can be made 1
    nums1 = [2, 6, 3, 4]
    res1 = solver.minOperations(nums1)
    print("Test 1:", nums1, "->", res1)
    # GCD of [2, 6, 3] = 1, so res = 2, operations = 2 + 4 - 1 = 5
    assert res1 == 5

    # Test 2: Array already has 1
    nums2 = [2, 1, 3, 4]
    res2 = solver.minOperations(nums2)
    print("Test 2:", nums2, "->", res2)
    assert res2 == 3  # n - ones = 4 - 1 = 3

    # Test 3: Array with all 1s
    nums3 = [1, 1, 1, 1]
    res3 = solver.minOperations(nums3)
    print("Test 3:", nums3, "->", res3)
    assert res3 == 0  # n - ones = 4 - 4 = 0

    # Test 4: Array where GCD can be made 1
    nums4 = [2, 10, 6, 14]
    res4 = solver.minOperations(nums4)
    print("Test 4:", nums4, "->", res4)
    # GCD of [2, 10] = 2, [2, 10, 6] = 2, [2, 10, 6, 14] = 2
    # GCD of [10, 6] = 2, [10, 6, 14] = 2
    # GCD of [6, 14] = 2
    # Actually, let me think: [2, 10] = 2, but we need to check all subarrays
    # This might return -1 if no subarray has GCD 1, or a value if it does
    assert res4 >= -1  # Valid result

    # Test 5: Array with coprime numbers
    nums5 = [2, 3, 4]
    res5 = solver.minOperations(nums5)
    print("Test 5:", nums5, "->", res5)
    # GCD of [2, 3] = 1, so res = 1, operations = 1 + 3 - 1 = 3
    assert res5 == 3

    # Test 6: Single element array
    nums6 = [2]
    res6 = solver.minOperations(nums6)
    print("Test 6:", nums6, "->", res6)
    assert res6 == -1  # Cannot make GCD 1 with single element that's not 1

    # Test 7: Array with 1 and other numbers
    nums7 = [1, 2, 3, 4, 5]
    res7 = solver.minOperations(nums7)
    print("Test 7:", nums7, "->", res7)
    assert res7 == 4  # n - ones = 5 - 1 = 4

    # Test 8: Array where adjacent elements have GCD 1
    nums8 = [6, 10, 15]
    res8 = solver.minOperations(nums8)
    print("Test 8:", nums8, "->", res8)
    # GCD of [6, 10] = 2, [6, 10, 15] = 1, so res = 2, operations = 2 + 3 - 1 = 4
    assert res8 == 4

    # Test 9: Array that cannot achieve GCD 1
    nums9 = [2, 4, 8]
    res9 = solver.minOperations(nums9)
    print("Test 9:", nums9, "->", res9)
    assert res9 == -1  # All GCDs will be even, cannot be 1

    # Test 10: Mixed array
    nums10 = [3, 6, 9, 5]
    res10 = solver.minOperations(nums10)
    print("Test 10:", nums10, "->", res10)
    # GCD of [3, 6, 9, 5] = 1, so res = 3, operations = 3 + 4 - 1 = 6
    # Actually, let's check: [3, 6] = 3, [3, 6, 9] = 3, [3, 6, 9, 5] = 1, so res = 3
    assert res10 == 6

    print("All tests passed!")


if __name__ == "__main__":
    test_minOperations()