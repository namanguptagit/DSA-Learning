class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if gcd(10, k)>1: return -1
        X=[1, 11, 111, 1111, 11111, 111111]
        l0=bisect.bisect_left(X, k)
        r=X[l0]%k
        len0=l0+1
        if r==0: return len0
        len0+=1
        while True:
            r=(10*r+1)%k
            if r==0: return len0
            len0+=1
    return -1
# Simple tests consistent with repository style (print + assert)
def test_smallestRepunitDivByK():
    solver = Solution()
    # Test 1: k = 1 -> should return 1 ("1" is divisible by 1)
    k1 = 1
    out1 = solver.smallestRepunitDivByK(k1)
    print("Test 1:", out1)
    assert out1 == 1

    # Test 2: k = 2 (impossible, ends with zeroes, gcd(10,2)>1)
    k2 = 2
    out2 = solver.smallestRepunitDivByK(k2)
    print("Test 2:", out2)
    assert out2 == -1

    # Test 3: k = 3 -> "111" is divisible by 3, so answer is 3
    k3 = 3
    out3 = solver.smallestRepunitDivByK(k3)
    print("Test 3:", out3)
    assert out3 == 3

    # Test 4: k = 7 -> should return 6 ("111111" is divisible by 7)
    k4 = 7
    out4 = solver.smallestRepunitDivByK(k4)
    print("Test 4:", out4)
    assert out4 == 6

    # Test 5: k = 13
    k5 = 13
    out5 = solver.smallestRepunitDivByK(k5)
    print("Test 5:", out5)
    assert out5 == 6

    # Test 6: k = 90 (gcd(10,90) = 10 > 1) should return -1
    k6 = 90
    out6 = solver.smallestRepunitDivByK(k6)
    print("Test 6:", out6)
    assert out6 == -1

    # Test 7: k = 17
    k7 = 17
    out7 = solver.smallestRepunitDivByK(k7)
    print("Test 7:", out7)
    assert out7 == 16

    print("All tests passed for smallestRepunitDivByK.")

if __name__ == "__main__":
    # Additional imports needed for the code to run
    import bisect
    from math import gcd
    test_smallestRepunitDivByK()