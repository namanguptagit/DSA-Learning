class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in s:
            if i == '*':
                ans.pop()
            else:
                ans.append(i)
        return "".join(ans)

# Simple tests consistent with repository style (print + assert)
def test_removeStars():
    solver = Solution()
    # Test 1: Example case
    s1 = "leet**cod*e"
    expected1 = "lecoe"
    out1 = solver.removeStars(s1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Remove only stars
    s2 = "erase*****"
    expected2 = ""
    out2 = solver.removeStars(s2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: No stars
    s3 = "abcde"
    expected3 = "abcde"
    out3 = solver.removeStars(s3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Star at end
    s4 = "ab*"
    expected4 = "a"
    out4 = solver.removeStars(s4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Alternating chars and stars
    s5 = "a*b*c*"
    expected5 = ""
    out5 = solver.removeStars(s5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: All stars removed by previous letters
    s6 = "abc*de*f*gh*"
    expected6 = "adg"
    out6 = solver.removeStars(s6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Empty string
    s7 = ""
    expected7 = ""
    out7 = solver.removeStars(s7)
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for removeStars.")

if __name__ == "__main__":
    test_removeStars()