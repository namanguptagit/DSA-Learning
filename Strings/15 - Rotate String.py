class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s

def test_rotateString():
    solver = Solution()

    # Test 1: Simple positive rotation
    s1 = "abcde"
    goal1 = "cdeab"
    expected1 = True
    out1 = solver.rotateString(s1, goal1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: No rotation (identical strings)
    s2 = "aaaa"
    goal2 = "aaaa"
    expected2 = True
    out2 = solver.rotateString(s2, goal2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Not a rotation
    s3 = "abcde"
    goal3 = "abced"
    expected3 = False
    out3 = solver.rotateString(s3, goal3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Empty strings
    s4 = ""
    goal4 = ""
    expected4 = True
    out4 = solver.rotateString(s4, goal4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Different lengths
    s5 = "abc"
    goal5 = "abcd"
    expected5 = False
    out5 = solver.rotateString(s5, goal5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Single character, same
    s6 = "a"
    goal6 = "a"
    expected6 = True
    out6 = solver.rotateString(s6, goal6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Single character, different
    s7 = "a"
    goal7 = "b"
    expected7 = False
    out7 = solver.rotateString(s7, goal7)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: All unique, negative
    s8 = "abcdef"
    goal8 = "fabcde"
    expected8 = True
    out8 = solver.rotateString(s8, goal8)
    print("Test 8:", out8)
    assert out8 == expected8

    print("All tests passed for rotateString.")

if __name__ == "__main__":
    test_rotateString()