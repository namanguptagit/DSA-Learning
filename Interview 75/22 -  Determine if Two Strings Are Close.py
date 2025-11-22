class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency_word1 = Counter(word1)
        frequency_word2 = Counter(word2)

        sorted_values_word1 = sorted(frequency_word1.values())
        sorted_values_word2 = sorted(frequency_word2.values())
      
        keys_match = set(frequency_word1.keys()) == set(frequency_word2.keys())

        return sorted_values_word1 == sorted_values_word2 and keys_match

# Simple tests consistent with repository style (print + assert)
def test_closeStrings():
    solver = Solution()
    
    # Test 1: simple positive case, anagram
    word1 = "abbzzca"
    word2 = "babzzac"
    expected1 = True
    out1 = solver.closeStrings(word1, word2)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: negative case, different letter set
    word1 = "abc"
    word2 = "bcd"
    expected2 = False
    out2 = solver.closeStrings(word1, word2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: positive case, swap frequencies is possible
    word1 = "aabbcc"
    word2 = "abcabc"
    expected3 = True
    out3 = solver.closeStrings(word1, word2)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: negative case, frequency match but keyset does not
    word1 = "aabbcc"
    word2 = "ddeeff"
    expected4 = False
    out4 = solver.closeStrings(word1, word2)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: both empty
    word1 = ""
    word2 = ""
    expected5 = True
    out5 = solver.closeStrings(word1, word2)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: one empty string, one not
    word1 = ""
    word2 = "a"
    expected6 = False
    out6 = solver.closeStrings(word1, word2)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: large positive case
    word1 = "zzzyyyxxxwww"
    word2 = "wwwxxyyzzzyx"
    expected7 = True
    out7 = solver.closeStrings(word1, word2)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: edge case, all chars single occurrence, same set
    word1 = "abcd"
    word2 = "badc"
    expected8 = True
    out8 = solver.closeStrings(word1, word2)
    print("Test 8:", out8)
    assert out8 == expected8

    # Test 9: different frequencies, same letters
    word1 = "aabbc"
    word2 = "aabbb"
    expected9 = False
    out9 = solver.closeStrings(word1, word2)
    print("Test 9:", out9)
    assert out9 == expected9

    print("All tests passed for closeStrings.")

if __name__ == "__main__":
    from collections import Counter
    test_closeStrings()