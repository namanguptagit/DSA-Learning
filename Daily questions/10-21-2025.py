from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOps: int) -> int:
        maxVal = max(nums) + k + 2
        count = [0] * maxVal

        for v in nums:
            count[v] += 1

        for i in range(1, maxVal):
            count[i] += count[i - 1]

        res = 0
        for i in range(maxVal):
            left = max(0, i - k)
            right = min(maxVal - 1, i + k)
            total = count[right] - (count[left - 1] if left else 0)
            freq = count[i] - (count[i - 1] if i else 0)
            res = max(res, freq + min(numOps, total - freq))

        return res


# Simple tests consistent with repository style (print + assert)
def test_maxFrequency():
    solver = Solution()

    # Test 1: Single element array
    nums1, k1, numOps1 = [1], 1, 1
    res1 = solver.maxFrequency(nums1, k1, numOps1)
    print("Test 1:", nums1, k1, numOps1, "->", res1)
    assert res1 == 1

    # Test 2: Two identical elements
    nums2, k2, numOps2 = [2, 2], 1, 1
    res2 = solver.maxFrequency(nums2, k2, numOps2)
    print("Test 2:", nums2, k2, numOps2, "->", res2)
    assert res2 == 2

    # Test 3: Two different elements with operations
    nums3, k3, numOps3 = [1, 2], 1, 1
    res3 = solver.maxFrequency(nums3, k3, numOps3)
    print("Test 3:", nums3, k3, numOps3, "->", res3)
    assert res3 == 2

    # Test 4: Multiple elements with no operations
    nums4, k4, numOps4 = [1, 2, 3, 4], 1, 0
    res4 = solver.maxFrequency(nums4, k4, numOps4)
    print("Test 4:", nums4, k4, numOps4, "->", res4)
    assert res4 == 1

    # Test 5: Multiple elements with operations
    nums5, k5, numOps5 = [1, 2, 3, 4], 1, 2
    res5 = solver.maxFrequency(nums5, k5, numOps5)
    print("Test 5:", nums5, k5, numOps5, "->", res5)
    assert res5 == 3

    # Test 6: Array with duplicates
    nums6, k6, numOps6 = [1, 1, 2, 2, 3], 1, 2
    res6 = solver.maxFrequency(nums6, k6, numOps6)
    print("Test 6:", nums6, k6, numOps6, "->", res6)
    assert res6 == 4

    # Test 7: Large k value
    nums7, k7, numOps7 = [1, 2, 3], 10, 1
    res7 = solver.maxFrequency(nums7, k7, numOps7)
    print("Test 7:", nums7, k7, numOps7, "->", res7)
    assert res7 == 3

    # Test 8: Large numOps value
    nums8, k8, numOps8 = [1, 2, 3, 4, 5], 1, 10
    res8 = solver.maxFrequency(nums8, k8, numOps8)
    print("Test 8:", nums8, k8, numOps8, "->", res8)
    assert res8 == 5

    print("All tests passed!")


if __name__ == "__main__":
    test_maxFrequency()