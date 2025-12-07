class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        # (low, high, expected_output)
        (1, 10, 5),        # 1,3,5,7,9
        (2, 8, 3),         # 3,5,7
        (3, 7, 3),         # 3,5,7
        (8, 10, 1),        # 9
        (2, 2, 0),         # 2 is not odd
        (3, 3, 1),         # 3 is odd
        (0, 0, 0),         # 0 is not odd
        (0, 1, 1),         # 1
        (0, 2, 1),         # 1
        (0, 3, 2),         # 1,3
        (1, 1, 1),         # 1
        (5, 5, 1),         # 5
        (100, 200, 51),    # All odds between 100 and 200
        (0, 1000000, 500000), # Large test
    ]
    for i, (low, high, expected) in enumerate(test_cases, 1):
        out = sol.countOdds(low, high)
        print(f"Test {i}: countOdds({low}, {high}) -> {out}")
        assert out == expected, f"Failed on test {i}"
    print("All tests passed for countOdds")