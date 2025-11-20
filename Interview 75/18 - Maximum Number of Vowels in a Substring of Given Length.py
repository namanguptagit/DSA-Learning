class Solution:
    def is_vowel(self, c: str) -> bool:
        return c in {'a', 'e', 'i', 'o', 'u'}

    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = 0
        left = 0
        vowel = 0

        for right in range(len(s)):
            if self.is_vowel(s[right]):
                vowel += 1

            if (right - left + 1) == k:
                max_vowel = max(max_vowel, vowel)
                if self.is_vowel(s[left]):
                    vowel -= 1
                left += 1

        return max_vowel
        # INSERT_YOUR_CODE
def test_maxVowels():
    solver = Solution()

    # Test 1: Example from LeetCode
    s1, k1 = "abciiidef", 3
    expected1 = 3
    out1 = solver.maxVowels(s1, k1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: All vowels
    s2, k2 = "aeiou", 2
    expected2 = 2
    out2 = solver.maxVowels(s2, k2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: No vowels
    s3, k3 = "bcdfg", 3
    expected3 = 0
    out3 = solver.maxVowels(s3, k3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: k equals length
    s4, k4 = "aebcdfi", 7
    expected4 = 3
    out4 = solver.maxVowels(s4, k4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Multiple windows, max in middle
    s5, k5 = "aeiobcdfu", 4
    expected5 = 4
    out5 = solver.maxVowels(s5, k5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Repeating characters
    s6, k6 = "zzzaeiouzzz", 5
    expected6 = 5
    out6 = solver.maxVowels(s6, k6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Mixed upper and lower (should only count lower-case vowels)
    s7, k7 = "AEIoUabcde", 5
    expected7 = 2  # only 'a' and 'e' are counted
    out7 = solver.maxVowels(s7, k7)
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for maxVowels.")

if __name__ == "__main__":
    test_maxVowels()