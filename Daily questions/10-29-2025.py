class Solution:
    def smallestNumber(self, n: int) -> int:
        k = 1
        while True:
            val = (1 << k) - 1
            if val >= n:
                return val
            k += 1


# Simple tests consistent with repository style (print + assert)
def test_smallestNumber():
    solver = Solution()

    # Test 1: n = 1 (returns 1 = 2^1 - 1)
    n1 = 1
    res1 = solver.smallestNumber(n1)
    print("Test 1:", n1, "->", res1)
    assert res1 == 1

    # Test 2: n = 2 (returns 3 = 2^2 - 1)
    n2 = 2
    res2 = solver.smallestNumber(n2)
    print("Test 2:", n2, "->", res2)
    assert res2 == 3

    # Test 3: n = 3 (returns 3 = 2^2 - 1)
    n3 = 3
    res3 = solver.smallestNumber(n3)
    print("Test 3:", n3, "->", res3)
    assert res3 == 3

    # Test 4: n = 4 (returns 7 = 2^3 - 1)
    n4 = 4
    res4 = solver.smallestNumber(n4)
    print("Test 4:", n4, "->", res4)
    assert res4 == 7

    # Test 5: n = 7 (returns 7 = 2^3 - 1)
    n5 = 7
    res5 = solver.smallestNumber(n5)
    print("Test 5:", n5, "->", res5)
    assert res5 == 7

    # Test 6: n = 8 (returns 15 = 2^4 - 1)
    n6 = 8
    res6 = solver.smallestNumber(n6)
    print("Test 6:", n6, "->", res6)
    assert res6 == 15

    # Test 7: n = 15 (returns 15 = 2^4 - 1)
    n7 = 15
    res7 = solver.smallestNumber(n7)
    print("Test 7:", n7, "->", res7)
    assert res7 == 15

    # Test 8: n = 16 (returns 31 = 2^5 - 1)
    n8 = 16
    res8 = solver.smallestNumber(n8)
    print("Test 8:", n8, "->", res8)
    assert res8 == 31

    # Test 9: n = 100 (returns 127 = 2^7 - 1)
    n9 = 100
    res9 = solver.smallestNumber(n9)
    print("Test 9:", n9, "->", res9)
    assert res9 == 127

    # Test 10: n = 500 (returns 511 = 2^9 - 1)
    n10 = 500
    res10 = solver.smallestNumber(n10)
    print("Test 10:", n10, "->", res10)
    assert res10 == 511

    print("All tests passed!")


if __name__ == "__main__":
    test_smallestNumber()