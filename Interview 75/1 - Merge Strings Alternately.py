class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        n1, n2 = len(word1), len(word2)
        
        for i in range(max(n1, n2)):
            if i < n1:
                result.append(word1[i])
            if i < n2:
                result.append(word2[i])
        return ''.join(result)


# Simple tests consistent with repository style (print + assert)
def test_mergeAlternately():
    solver = Solution()

    cases = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("", "abc", "abc"),
        ("abc", "", "abc"),
    ]

    for a, b, expected in cases:
        res = solver.mergeAlternately(a, b)
        print(f"mergeAlternately({a!r}, {b!r}) -> {res}")
        assert res == expected

    print("All tests passed for mergeAlternately")


if __name__ == "__main__":
    test_mergeAlternately()