class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        # find first & last
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        res = 0

        for c in range(26):
            L, R = first[c], last[c]
            if R - L < 2:
                continue

            seen = [False] * 26

            for i in range(L + 1, R):
                idx = ord(s[i]) - ord('a')
                if not seen[idx]:
                    seen[idx] = True
                    res += 1

        return res

# Simple tests consistent with repository style (print + assert)
def test_countPalindromicSubsequence():
    solver = Solution()

    # Test 1: Simple example, all unique
    s1 = "aabca"
    expected1 = 3  # "aba","aca","aaa"
    out1 = solver.countPalindromicSubsequence(s1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Letters all same
    s2 = "aaaa"
    expected2 = 1  # Only "aaa"
    out2 = solver.countPalindromicSubsequence(s2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Example with no palindromic length-3
    s3 = "abc"
    expected3 = 0
    out3 = solver.countPalindromicSubsequence(s3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Large repeat letters
    s4 = "ababa"
    expected4 = 2  # "aaa", "aba"
    out4 = solver.countPalindromicSubsequence(s4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Palindrome with more inside
    s5 = "abcba"
    expected5 = 3  # "aba", "aca", "aba" (but unique: "aba", "aca", "aba") -> unique 2? Let's check:
    # "a_a", "a_b", "a_c" inside "a___a" range, possibilities: "aba", "aca", "aba"
    # but only count unique middle, so for 'a': 'b','c' inside 'a___a' => 2
    # for 'b': inside 'b___b' is 'c' => "bcb"
    # total: 'a':b,c = 2, 'b':c = 1, so expected = 3
    out5 = solver.countPalindromicSubsequence(s5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Empty string
    s6 = ""
    expected6 = 0
    out6 = solver.countPalindromicSubsequence(s6)
    print("Test 6:", out6)
    assert out6 == expected6

    print("All tests passed for countPalindromicSubsequence.")

if __name__ == "__main__":
    test_countPalindromicSubsequence()