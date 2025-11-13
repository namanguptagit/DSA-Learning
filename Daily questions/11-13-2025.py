class Solution:
    def maxOperations(self, s: str) -> int:
        count_one = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == "0":
                while i + 1 < len(s) and s[i + 1] == "0":
                    i += 1
                ans += count_one
            else:
                count_one += 1
            i += 1
        return ans


# Simple tests consistent with repository style (print + assert)
def test_maxOperations():
    solver = Solution()

    # Test 1: Basic example
    s1 = "010"
    res1 = solver.maxOperations(s1)
    print("Test 1:", s1, "->", res1)
    assert res1 == 1  # One '1' before first '0', so 1 operation

    # Test 2: Multiple zeros
    s2 = "0010"
    res2 = solver.maxOperations(s2)
    print("Test 2:", s2, "->", res2)
    assert res2 == 0  # No '1's before zeros

    # Test 3: Multiple ones before zeros
    s3 = "1100"
    res3 = solver.maxOperations(s3)
    print("Test 3:", s3, "->", res3)
    assert res3 == 2  # Two '1's before zeros, so 2 operations

    # Test 4: Alternating pattern
    s4 = "1010"
    res4 = solver.maxOperations(s4)
    print("Test 4:", s4, "->", res4)
    assert res4 == 3  # One '1' before first '0' (1), two '1's before second '0' (2), total 3

    # Test 5: All ones
    s5 = "111"
    res5 = solver.maxOperations(s5)
    print("Test 5:", s5, "->", res5)
    assert res5 == 0  # No zeros, so no operations

    # Test 6: All zeros
    s6 = "000"
    res6 = solver.maxOperations(s6)
    print("Test 6:", s6, "->", res6)
    assert res6 == 0  # No ones, so no operations

    # Test 7: Single character
    s7 = "0"
    res7 = solver.maxOperations(s7)
    print("Test 7:", s7, "->", res7)
    assert res7 == 0  # No ones before zero

    # Test 8: Single one
    s8 = "1"
    res8 = solver.maxOperations(s8)
    print("Test 8:", s8, "->", res8)
    assert res8 == 0  # No zeros

    # Test 9: Complex pattern
    s9 = "101100"
    res9 = solver.maxOperations(s9)
    print("Test 9:", s9, "->", res9)
    assert res9 == 4  # One '1' before first '0' (1), three '1's before second group of zeros (3), total 4

    # Test 10: Multiple groups
    s10 = "11001100"
    res10 = solver.maxOperations(s10)
    print("Test 10:", s10, "->", res10)
    assert res10 == 6  # Two '1's before first zeros (2), four '1's before second zeros (4), total 6

    # Test 11: Ones after zeros
    s11 = "0011"
    res11 = solver.maxOperations(s11)
    print("Test 11:", s11, "->", res11)
    assert res11 == 0  # No ones before zeros

    # Test 12: Long string
    s12 = "111000111000"
    res12 = solver.maxOperations(s12)
    print("Test 12:", s12, "->", res12)
    assert res12 == 9  # Three '1's before first zeros (3), six '1's before second zeros (6), total 9

    print("All tests passed!")


if __name__ == "__main__":
    test_maxOperations()