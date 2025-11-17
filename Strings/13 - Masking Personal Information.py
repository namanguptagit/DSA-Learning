class Solution:
    def maskPII(self, s: str) -> str:
        s = s.strip()
        
        # Case 1: Email
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            return name[0] + "*****" + name[-1] + "@" + domain
        
        # Case 2: Phone number
        digits = [c for c in s if c.isdigit()]
        n = len(digits)
        last4 = "".join(digits[-4:])
        
        # domestic number (10 digits)
        if n == 10:
            return "***-***-" + last4
        
        # international number
        country = n - 10
        return "+" + "*" * country + "-***-***-" + last4
# Simple tests consistent with repository style (print + assert)
def test_maskPII():
    solver = Solution()

    # Test 1: Email Lowercase
    s1 = "LeetCode@LeetCode.com"
    expected1 = "l*****e@leetcode.com"
    out1 = solver.maskPII(s1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Email with uppercase and spaces
    s2 = "  AB@DOMAIN.COM "
    expected2 = "a*****b@domain.com"
    out2 = solver.maskPII(s2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Domestic phone (10 digits)
    s3 = "123-456-7890"
    expected3 = "***-***-7890"
    out3 = solver.maskPII(s3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: US phone, mixed symbols
    s4 = "(123) 456-7890"
    expected4 = "***-***-7890"
    out4 = solver.maskPII(s4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: International phone, 11 digits
    s5 = "+1 (234) 567-8901"
    expected5 = "+*-***-***-8901"
    out5 = solver.maskPII(s5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: International phone, 12 digits
    s6 = "+91 234-567-8901"
    expected6 = "+**-***-***-8901"
    out6 = solver.maskPII(s6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: International phone, 13 digits
    s7 = "+886-123-456-7890"
    expected7 = "+***-***-***-7890"
    out7 = solver.maskPII(s7)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: Email, 1 character before and after asterisk
    s8 = "Xy@e.co"
    expected8 = "x*****y@e.co"
    out8 = solver.maskPII(s8)
    print("Test 8:", out8)
    assert out8 == expected8

    # Test 9: Email, already lowercase
    s9 = "bob@abc.com"
    expected9 = "b*****b@abc.com"
    out9 = solver.maskPII(s9)
    print("Test 9:", out9)
    assert out9 == expected9

    # Test 10: Phone, minimal symbols, 10 digits
    s10 = "0123456789"
    expected10 = "***-***-6789"
    out10 = solver.maskPII(s10)
    print("Test 10:", out10)
    assert out10 == expected10

    print("All tests passed for maskPII.")

if __name__ == "__main__":
    test_maskPII()
