class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        return self.decode(s)
    def decode(self, s: str) -> str:
        res, num = "", 0
        while self.i < len(s):
            c = s[self.i]
            if c.isdigit():
                num = num * 10 + int(c)
                self.i += 1
            elif c == '[':
                self.i += 1
                inner = self.decode(s)
                res += inner * num
                num = 0
            elif c == ']':
                self.i += 1
                return res
            else:
                res += c
                self.i += 1
        return res
        # INSERT_YOUR_CODE
# Simple tests consistent with repository style (print + assert)
def test_decodeString():
    solver = Solution()
    # Test 1: Example case
    s1 = "3[a]2[bc]"
    expected1 = "aaabcbc"
    out1 = solver.decodeString(s1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Nested brackets
    s2 = "3[a2[c]]"
    expected2 = "accaccacc"
    out2 = solver.decodeString(s2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Multiple groups
    s3 = "2[abc]3[cd]ef"
    expected3 = "abcabccdcdcdef"
    out3 = solver.decodeString(s3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: No brackets, just string
    s4 = "abc"
    expected4 = "abc"
    out4 = solver.decodeString(s4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Deeply nested
    s5 = "2[a2[b2[c]]]"
    expected5 = "abccbccabccbcc"
    out5 = solver.decodeString(s5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Single number group with chars after
    s6 = "10[a]b"
    expected6 = "aaaaaaaaaab"
    out6 = solver.decodeString(s6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Empty brackets (should not realistically happen but check)
    s7 = "2[]abc"
    expected7 = "abc"
    out7 = solver.decodeString(s7)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: Multiple digits in reps
    s8 = "12[x]"
    expected8 = "xxxxxxxxxxxx"
    out8 = solver.decodeString(s8)
    print("Test 8:", out8)
    assert out8 == expected8

    # Test 9: No input
    s9 = ""
    expected9 = ""
    out9 = solver.decodeString(s9)
    print("Test 9:", out9)
    assert out9 == expected9

    print("All tests passed for decodeString.")

if __name__ == "__main__":
    test_decodeString()