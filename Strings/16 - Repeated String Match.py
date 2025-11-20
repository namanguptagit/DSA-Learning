class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1
        repeated = a
        
        # Repeat 'a' till its length >= b
        while len(repeated) < len(b):
            repeated += a
            count += 1
        
        # Now check if b is a substring
        if b in repeated:
            return count
        
        # Try one more repetition to cover edge case
        repeated += a
        if b in repeated:
            return count + 1
        
        return -1
        # INSERT_YOUR_CODE
def test_repeatedStringMatch():
    solver = Solution()
    
    # Test 1: Canonical repeat
    a1, b1 = "abcd", "cdabcdab"
    expected1 = 3  # "abcdabcdabcd" contains "cdabcdab"
    out1 = solver.repeatedStringMatch(a1, b1)
    print("Test 1:", out1)
    assert out1 == expected1
    
    # Test 2: b shorter, no repeat needed
    a2, b2 = "abc", "abc"
    expected2 = 1
    out2 = solver.repeatedStringMatch(a2, b2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Impossible to cover
    a3, b3 = "a", "aaab"
    expected3 = -1
    out3 = solver.repeatedStringMatch(a3, b3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: b not a substring even after sufficient repeats
    a4, b4 = "abc", "ac"
    expected4 = -1
    out4 = solver.repeatedStringMatch(a4, b4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: b same as a, single repeat
    a5, b5 = "xyz", "xyz"
    expected5 = 1
    out5 = solver.repeatedStringMatch(a5, b5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: b is a substring after 2 repeats, with overlap
    a6, b6 = "abc", "cabca"
    expected6 = 3
    out6 = solver.repeatedStringMatch(a6, b6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Both empty
    a7, b7 = "", ""
    # according to logic, if both empty, after 1 repeat "" contains ""
    expected7 = 1
    out7 = solver.repeatedStringMatch(a7, b7)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: b longer than a but impossible to build
    a8, b8 = "abc", "bcabx"
    expected8 = -1
    out8 = solver.repeatedStringMatch(a8, b8)
    print("Test 8:", out8)
    assert out8 == expected8

    print("All tests passed for repeatedStringMatch.")

if __name__ == "__main__":
    test_repeatedStringMatch()