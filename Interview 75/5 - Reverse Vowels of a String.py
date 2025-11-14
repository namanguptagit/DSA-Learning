class Solution:
    def reverseVowels(self, s: str) -> str:
        stringList = list(s)
        left, right = 0, len(s) - 1
        vowels = 'aAeEiIoOuU'

        while left < right:
            if stringList[left] in vowels and stringList[right] in vowels:
                stringList[left], stringList[right] = stringList[right], stringList[left]
                left += 1
                right -= 1
            elif stringList[left] not in vowels:
                left += 1
            elif stringList[right] not in vowels:
                right -= 1
        
        return ''.join(stringList)

# Simple tests consistent with repository style (print + assert)
def test_reverseVowels():
    solver = Solution()

    # Test 1: Standard example, LeetCode
    s1 = "hello"
    expected1 = "holle"
    res1 = solver.reverseVowels(s1)
    print("Test 1:", res1)
    assert res1 == expected1

    # Test 2: All vowels
    s2 = "aeiou"
    expected2 = "uoiea"
    res2 = solver.reverseVowels(s2)
    print("Test 2:", res2)
    assert res2 == expected2

    # Test 3: No vowels
    s3 = "bcdfg"
    expected3 = "bcdfg"
    res3 = solver.reverseVowels(s3)
    print("Test 3:", res3)
    assert res3 == expected3

    # Test 4: Palindrome with vowels
    s4 = "racecar"
    expected4 = "racecar"
    res4 = solver.reverseVowels(s4)
    print("Test 4:", res4)
    assert res4 == expected4

    # Test 5: Mixed case vowels
    s5 = "lEetcOde"
    expected5 = "lOetcEde"
    res5 = solver.reverseVowels(s5)
    print("Test 5:", res5)
    assert res5 == expected5

    # Test 6: Empty string
    s6 = ""
    expected6 = ""
    res6 = solver.reverseVowels(s6)
    print("Test 6:", res6)
    assert res6 == expected6

    # Test 7: Single character, vowel
    s7 = "a"
    expected7 = "a"
    res7 = solver.reverseVowels(s7)
    print("Test 7:", res7)
    assert res7 == expected7

    # Test 8: Single character, non-vowel
    s8 = "b"
    expected8 = "b"
    res8 = solver.reverseVowels(s8)
    print("Test 8:", res8)
    assert res8 == expected8

    # Test 9: Repeated vowels and consonants
    s9 = "banana"
    expected9 = "banana"
    res9 = solver.reverseVowels(s9)
    print("Test 9:", res9)
    assert res9 == expected9

if __name__ == "__main__":
    test_reverseVowels()