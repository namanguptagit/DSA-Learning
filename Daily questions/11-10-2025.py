class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stack = []
        res = 0
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            if n == 0:
                continue
            if not stack or stack[-1] < n:
                res += 1
                stack.append(n)
        return res


# Simple tests consistent with repository style (print + assert)
def test_minOperations():
    solver = Solution()

    # Test 1: Empty array
    nums1 = []
    res1 = solver.minOperations(nums1)
    print("Test 1: nums=", nums1, "->", res1)
    assert res1 == 0

    # Test 2: Single element
    nums2 = [1]
    res2 = solver.minOperations(nums2)
    print("Test 2: nums=", nums2, "->", res2)
    assert res2 == 1

    # Test 3: Strictly increasing sequence
    nums3 = [1, 2, 3, 4]
    res3 = solver.minOperations(nums3)
    print("Test 3: nums=", nums3, "->", res3)
    assert res3 == 4

    # Test 4: Strictly decreasing sequence
    nums4 = [4, 3, 2, 1]
    res4 = solver.minOperations(nums4)
    print("Test 4: nums=", nums4, "->", res4)
    assert res4 == 4

    # Test 5: All zeros
    nums5 = [0, 0, 0]
    res5 = solver.minOperations(nums5)
    print("Test 5: nums=", nums5, "->", res5)
    assert res5 == 0

    # Test 6: Zeros mixed with numbers
    nums6 = [0, 1, 0, 2, 0, 3]
    res6 = solver.minOperations(nums6)
    print("Test 6: nums=", nums6, "->", res6)
    assert res6 == 3

    # Test 7: Duplicate values (non-increasing)
    nums7 = [1, 1, 1]
    res7 = solver.minOperations(nums7)
    print("Test 7: nums=", nums7, "->", res7)
    assert res7 == 1

    # Test 8: Mixed increasing and decreasing
    nums8 = [3, 1, 2, 4, 2, 5]
    res8 = solver.minOperations(nums8)
    print("Test 8: nums=", nums8, "->", res8)
    assert res8 == 4

    # Test 9: All same non-zero values
    nums9 = [5, 5, 5, 5]
    res9 = solver.minOperations(nums9)
    print("Test 9: nums=", nums9, "->", res9)
    assert res9 == 1

    # Test 10: Complex case with zeros and duplicates
    nums10 = [2, 1, 0, 3, 2, 4, 0, 1]
    res10 = solver.minOperations(nums10)
    print("Test 10: nums=", nums10, "->", res10)
    assert res10 == 4

    print("All tests passed!")


if __name__ == "__main__":
    test_minOperations()