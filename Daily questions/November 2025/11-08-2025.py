class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans=0
        while n:
            ans=-ans-(n^(n-1))
            n&=n-1
        return abs(ans)


# Simple tests consistent with repository style (print + assert)
def test_minimumOneBitOperations():
    solver = Solution()

    # Test 1: n = 0 (already zero)
    n1 = 0
    res1 = solver.minimumOneBitOperations(n1)
    print("Test 1: n=", n1, "->", res1)
    assert res1 == 0

    # Test 2: n = 1 (single bit set)
    n2 = 1
    res2 = solver.minimumOneBitOperations(n2)
    print("Test 2: n=", n2, "->", res2)
    assert res2 == 1

    # Test 3: n = 2 (10 in binary)
    n3 = 2
    res3 = solver.minimumOneBitOperations(n3)
    print("Test 3: n=", n3, "->", res3)
    assert res3 == 3

    # Test 4: n = 3 (11 in binary)
    n4 = 3
    res4 = solver.minimumOneBitOperations(n4)
    print("Test 4: n=", n4, "->", res4)
    assert res4 == 2

    # Test 5: n = 4 (100 in binary, power of 2)
    n5 = 4
    res5 = solver.minimumOneBitOperations(n5)
    print("Test 5: n=", n5, "->", res5)
    assert res5 == 7

    # Test 6: n = 5 (101 in binary)
    n6 = 5
    res6 = solver.minimumOneBitOperations(n6)
    print("Test 6: n=", n6, "->", res6)
    assert res6 == 6

    # Test 7: n = 6 (110 in binary)
    n7 = 6
    res7 = solver.minimumOneBitOperations(n7)
    print("Test 7: n=", n7, "->", res7)
    assert res7 == 4

    # Test 8: n = 7 (111 in binary, all bits set)
    n8 = 7
    res8 = solver.minimumOneBitOperations(n8)
    print("Test 8: n=", n8, "->", res8)
    assert res8 == 5

    # Test 9: n = 8 (1000 in binary, power of 2)
    n9 = 8
    res9 = solver.minimumOneBitOperations(n9)
    print("Test 9: n=", n9, "->", res9)
    assert res9 == 15

    # Test 10: Larger number
    n10 = 15
    res10 = solver.minimumOneBitOperations(n10)
    print("Test 10: n=", n10, "->", res10)
    assert res10 == 10

    print("All tests passed!")


if __name__ == "__main__":
    test_minimumOneBitOperations()  