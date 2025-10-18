class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f = float('-inf')
        r = 0
        nums.sort()
        for i in nums:
            l = i - k
            u = i + k
            if f < l:
                f = l
                r += 1
            elif f < u:
                f += 1
                r += 1
        return r


# Simple tests consistent with repository style (print + assert)
def test_maxDistinctElements():
    solver = Solution()

    # Test 1: Single element -> 1
    nums1, k1 = [1], 1
    res1 = solver.maxDistinctElements(nums1, k1)
    print("Test 1:", nums1, k1, "->", res1)
    assert res1 == 1

    # Test 2: Two elements with k=1 -> 2
    nums2, k2 = [1, 2], 1
    res2 = solver.maxDistinctElements(nums2, k2)
    print("Test 2:", nums2, k2, "->", res2)
    assert res2 == 2

    # Test 3: Two elements with k=0 -> 2
    nums3, k3 = [1, 2], 0
    res3 = solver.maxDistinctElements(nums3, k3)
    print("Test 3:", nums3, k3, "->", res3)
    assert res3 == 2

    # Test 4: Three elements with k=1 -> 2 (overlapping ranges)
    nums4, k4 = [1, 2, 3], 1
    res4 = solver.maxDistinctElements(nums4, k4)
    print("Test 4:", nums4, k4, "->", res4)
    assert res4 == 2

    # Test 5: Three elements with k=0 -> 3
    nums5, k5 = [1, 2, 3], 0
    res5 = solver.maxDistinctElements(nums5, k5)
    print("Test 5:", nums5, k5, "->", res5)
    assert res5 == 3

    # Test 6: Unsorted array -> should work after sorting
    nums6, k6 = [3, 1, 2], 1
    res6 = solver.maxDistinctElements(nums6, k6)
    print("Test 6:", nums6, k6, "->", res6)
    assert res6 == 2

    # Test 7: Large k value -> 1 (all elements overlap)
    nums7, k7 = [1, 2, 3], 10
    res7 = solver.maxDistinctElements(nums7, k7)
    print("Test 7:", nums7, k7, "->", res7)
    assert res7 == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_maxDistinctElements()