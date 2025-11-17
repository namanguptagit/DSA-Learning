class Solution:
    def detectCapitalUse(self, word: str) -> bool:
       return (word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()))

# Simple tests consistent with repository style (print + assert)
def test_detectCapitalUse():
    solver = Solution()

    # Test 1: All uppercase
    word1 = "USA"
    expected1 = True
    out1 = solver.detectCapitalUse(word1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: All lowercase
    word2 = "leetcode"
    expected2 = True
    out2 = solver.detectCapitalUse(word2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: First letter uppercase, rest lowercase
    word3 = "Google"
    expected3 = True
    out3 = solver.detectCapitalUse(word3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Invalid usage
    word4 = "FlaG"
    expected4 = False
    out4 = solver.detectCapitalUse(word4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Single uppercase letter
    word5 = "A"
    expected5 = True
    out5 = solver.detectCapitalUse(word5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Single lowercase letter
    word6 = "z"
    expected6 = True
    out6 = solver.detectCapitalUse(word6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Two uppercase followed by lowercase
    word7 = "USa"
    expected7 = False
    out7 = solver.detectCapitalUse(word7)
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for detectCapitalUse.")

if __name__ == "__main__":
    test_detectCapitalUse()