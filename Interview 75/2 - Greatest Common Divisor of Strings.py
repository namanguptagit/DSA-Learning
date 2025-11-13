class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])


# Simple tests consistent with repository style (print + assert)
def test_gcdOfStrings():
    solver = Solution()

    cases = [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
        ("ABAB", "AB", "AB"),
        ("", "", ""),
    ]

    for a, b, expected in cases:
        res = solver.gcdOfStrings(a, b)
        print(f"gcdOfStrings({a!r}, {b!r}) -> {res!r}")
        assert res == expected

    print("All tests passed for gcdOfStrings")


if __name__ == "__main__":
    test_gcdOfStrings()