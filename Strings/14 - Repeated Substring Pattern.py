class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

def test_repeatedSubstringPattern():
    solver = Solution()
    # Test 1: Canonical "abab"
    s1 = "abab"
    expected1 = True
    out1 = solver.repeatedSubstringPattern(s1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Single character (cannot be a repeated substring)
    s2 = "a"
    expected2 = False
    out2 = solver.repeatedSubstringPattern(s2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: All identical characters, repeated
    s3 = "aaaa"
    expected3 = True
    out3 = solver.repeatedSubstringPattern(s3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Not repeated
    s4 = "abc"
    expected4 = False
    out4 = solver.repeatedSubstringPattern(s4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: "abcabcabcabc"
    s5 = "abcabcabcabc"
    expected5 = True
    out5 = solver.repeatedSubstringPattern(s5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Long, NOT a repeat
    s6 = "abac"
    expected6 = False
    out6 = solver.repeatedSubstringPattern(s6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Edge, repeated single letter but not for whole string
    s7 = "aaab"
    expected7 = False
    out7 = solver.repeatedSubstringPattern(s7)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: Empty string (though not in normal constraints)
    s8 = ""
    expected8 = False
    out8 = solver.repeatedSubstringPattern(s8)
    print("Test 8:", out8)
    assert out8 == expected8

    print("All tests passed for repeatedSubstringPattern.")


if __name__ == "__main__":
    test_repeatedSubstringPattern()