class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

# Simple tests consistent with repository style (print + assert)
def test_isSubsequence():
    solver = Solution()

    # Test 1: s is a subsequence of t
    s1, t1 = "abc", "ahbgdc"
    expected1 = True
    out1 = solver.isSubsequence(s1, t1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: s is not a subsequence of t
    s2, t2 = "axc", "ahbgdc"
    expected2 = False
    out2 = solver.isSubsequence(s2, t2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: empty s is always a subsequence
    s3, t3 = "", "anything"
    expected3 = True
    out3 = solver.isSubsequence(s3, t3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: t is empty, s non-empty
    s4, t4 = "a", ""
    expected4 = False
    out4 = solver.isSubsequence(s4, t4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: s and t are both empty
    s5, t5 = "", ""
    expected5 = True
    out5 = solver.isSubsequence(s5, t5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: s is equal to t
    s6, t6 = "a", "a"
    expected6 = True
    out6 = solver.isSubsequence(s6, t6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: s letters appear out of order in t
    s7, t7 = "acb", "ahbgdc"
    expected7 = False
    out7 = solver.isSubsequence(s7, t7)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: s longer than t
    s8, t8 = "abcd", "abc"
    expected8 = False
    out8 = solver.isSubsequence(s8, t8)
    print("Test 8:", out8)
    assert out8 == expected8

    print("All tests passed for isSubsequence.")

if __name__ == "__main__":
    test_isSubsequence()