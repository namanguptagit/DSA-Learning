class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums)%k

# ---- Simple tests consistent with repository style (print + assert) ----
def test_minOperations():
    solver = Solution()
    # Test 1: Example, sum divisible
    out1 = solver.minOperations([1,2,3,4], 5)  # sum=10, 10%5=0
    print("Test 1:", out1)
    assert out1 == 0

    # Test 2: Not divisible
    out2 = solver.minOperations([2,4,7], 4)  # sum=13, 13%4=1
    print("Test 2:", out2)
    assert out2 == 1

    # Test 3: k = 1 (always zero)
    out3 = solver.minOperations([1,2,3], 1)
    print("Test 3:", out3)
    assert out3 == 0

    # Test 4: Negative numbers
    out4 = solver.minOperations([3,-1,2], 4)  # sum=4, 4%4=0
    print("Test 4:", out4)
    assert out4 == 0

    # Test 5: Empty list, k=3
    out5 = solver.minOperations([], 3)  # sum=0, 0%3=0
    print("Test 5:", out5)
    assert out5 == 0

# Uncomment to run tests
# test_minOperations()