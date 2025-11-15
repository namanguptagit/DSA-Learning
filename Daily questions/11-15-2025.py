class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res

# Test cases
test_cases = [
    ("001", 3),  # Example where the string has a mix of '0's and '1's.
    ("000", 6),  # All '0's
    ("111", 0),  # All '1's, should not have any valid substrings.
    ("101010", 9),  # A mix of 1's and 0's
    ("1101", 4),  # Another mix with more '1's.
    ("111001", 12),  # Mixed with multiple zeros.
    ("000000", 21),  # Multiple zeroes.
    ("1", 0),  # Single '1'
    ("0", 1),  # Single '0'
]

# Create an instance of Solution and run the test cases
solution = Solution()
for i, (s, expected) in enumerate(test_cases):
    result = solution.numberOfSubstrings(s)
    print(f"Test case {i + 1}: input = '{s}', expected = {expected}, got = {result}")
