class Solution:
    def productExceptSelf(self, nums: List[int]) -> list[int]:
        n = len(nums)
        res = []
        prefix = [1] * (n+1)
        suffix = [1] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        return res

# Simple tests consistent with repository style (print + assert)
def test_productExceptSelf():
    solver = Solution()

    # Test 1: Example from LeetCode
    nums1 = [1,2,3,4]
    expected1 = [24,12,8,6]
    res1 = solver.productExceptSelf(nums1)
    print("Test 1:", res1)
    assert res1 == expected1

    # Test 2: Contains zero
    nums2 = [0,1,2,3]
    expected2 = [6,0,0,0]
    res2 = solver.productExceptSelf(nums2)
    print("Test 2:", res2)
    assert res2 == expected2

    # Test 3: All ones
    nums3 = [1,1,1,1]
    expected3 = [1,1,1,1]
    res3 = solver.productExceptSelf(nums3)
    print("Test 3:", res3)
    assert res3 == expected3

    # Test 4: Two numbers
    nums4 = [4,2]
    expected4 = [2,4]
    res4 = solver.productExceptSelf(nums4)
    print("Test 4:", res4)
    assert res4 == expected4

    # Test 5: Negative numbers
    nums5 = [-1,1,0,-3,3]
    expected5 = [0,0,9,0,0]
    res5 = solver.productExceptSelf(nums5)
    print("Test 5:", res5)
    assert res5 == expected5

    # Test 6: Single element (edge, though not per constraints >1)
    nums6 = [42]
    expected6 = [1]
    res6 = solver.productExceptSelf(nums6)
    print("Test 6:", res6)
    assert res6 == expected6

    print("All tests passed for productExceptSelf.")

if __name__ == "__main__":
    test_productExceptSelf()