class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0

        mp = {0: -1}
        prefix = 0
        res = len(nums)

        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            need = (prefix - target + p) % p

            if need in mp:
                res = min(res, i - mp[need])

            mp[prefix] = i

        return -1 if res == len(nums) else res

# ---- Simple tests consistent with repository style (print + assert) ----
def test_minSubarray():
    solver = Solution()
    # Test 1: Example from LeetCode (need to remove [3])
    out1 = solver.minSubarray([3,1,4,2], 6) 
    print("Test 1:", out1)
    assert out1 == 1

    # Test 2: Need to remove [2,2] (total=7, 7%3=1, must remove sum%3==1, best is [3])
    out2 = solver.minSubarray([6,3,5,2], 9)
    print("Test 2:", out2)
    assert out2 == 2

    # Test 3: No need to remove anything (sum%p==0)
    out3 = solver.minSubarray([1,2,3], 6)
    print("Test 3:", out3)
    assert out3 == 0

    # Test 4: Impossible (must remove all)
    out4 = solver.minSubarray([1,2,3], 5)
    print("Test 4:", out4)
    assert out4 == -1

    # Test 5: Only one number must be removed (last)
    out5 = solver.minSubarray([1,2,3], 3)
    print("Test 5:", out5)
    assert out5 == 0

    # Test 6: Large p (impossible)
    out6 = solver.minSubarray([6,2,4,8], 100)
    print("Test 6:", out6)
    assert out6 == -1

    # Test 7: Remove long prefix
    out7 = solver.minSubarray([5,7,8,6,8], 7)
    print("Test 7:", out7)
    # sum=34 % 7 = 6, best to remove [7,8,6,8]=29, length=4
    assert out7 == 1

    # Test 8: All zeroes
    out8 = solver.minSubarray([0, 0, 0, 0], 1)
    print("Test 8:", out8)
    assert out8 == 0

# Uncomment to run tests
# test_minSubarray()