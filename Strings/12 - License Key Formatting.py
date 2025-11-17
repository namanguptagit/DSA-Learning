class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        first = len(s) % k
        
        ans = []
        if first:
            ans.append(s[:first])
        
        for i in range(first, len(s), k):
            ans.append(s[i:i+k])
        
        return "-".join(ans)

# Simple tests consistent with repository style (print + assert)
def test_licenseKeyFormatting():
    solver = Solution()

    # Test 1: Example input from LeetCode
    s1 = "5F3Z-2e-9-w"
    k1 = 4
    expected1 = "5F3Z-2E9W"
    out1 = solver.licenseKeyFormatting(s1, k1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Example with first group shorter
    s2 = "2-5g-3-J"
    k2 = 2
    expected2 = "2-5G-3J"
    out2 = solver.licenseKeyFormatting(s2, k2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Input with only dashes
    s3 = "---"
    k3 = 3
    expected3 = ""
    out3 = solver.licenseKeyFormatting(s3, k3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Single group, no dash needed
    s4 = "abc"
    k4 = 5
    expected4 = "ABC"
    out4 = solver.licenseKeyFormatting(s4, k4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Already well-formed, upper case
    s5 = "ABCDE"
    k5 = 5
    expected5 = "ABCDE"
    out5 = solver.licenseKeyFormatting(s5, k5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Only one character
    s6 = "a"
    k6 = 2
    expected6 = "A"
    out6 = solver.licenseKeyFormatting(s6, k6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Long string with mixed lower and upper
    s7 = "a-a-a-a-"
    k7 = 2
    expected7 = "AA-AA"
    out7 = solver.licenseKeyFormatting(s7, k7)
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for licenseKeyFormatting.")

if __name__ == "__main__":
    test_licenseKeyFormatting()