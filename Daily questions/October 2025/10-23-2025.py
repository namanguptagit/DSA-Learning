class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(digits) for digits in s]
        n = len(s)
        binomial_coeff = [1] * (n - 1)
        # recursive definition of the coefficients
        for i in range(1, n - 1):
            binomial_coeff[i] = binomial_coeff[i-1] * (n-2-i+1) // i
        
        left = sum([digit*coeff for digit, coeff in zip(s[:-1], binomial_coeff)]) % 10
        right = sum([digit*coeff for digit, coeff in zip(s[1:], binomial_coeff)]) % 10
        return left == right


# Simple tests consistent with repository style (print + assert)
def test_hasSameDigits():
    solver = Solution()

    # Test 1: Single digit (trivial true)
    s1 = "0"
    r1 = solver.hasSameDigits(s1)
    print("Test 1:", s1, "->", r1)
    assert r1 is True

    # Test 2: Two identical digits
    s2 = "11"
    r2 = solver.hasSameDigits(s2)
    print("Test 2:", s2, "->", r2)
    assert r2 is True

    # Test 3: Two different digits
    s3 = "12"
    r3 = solver.hasSameDigits(s3)
    print("Test 3:", s3, "->", r3)
    assert r3 is False

    # Test 4: Palindromic three digits that satisfy condition
    s4 = "121"
    r4 = solver.hasSameDigits(s4)
    print("Test 4:", s4, "->", r4)
    assert r4 is True

    # Test 5: Three digits not satisfying condition
    s5 = "123"
    r5 = solver.hasSameDigits(s5)
    print("Test 5:", s5, "->", r5)
    assert r5 is False

    # Test 6: Repeated digits
    s6 = "9999"
    r6 = solver.hasSameDigits(s6)
    print("Test 6:", s6, "->", r6)
    assert r6 is True

    print("All tests passed!")


if __name__ == "__main__":
    test_hasSameDigits()