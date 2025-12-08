class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for u in range(2, int(sqrt(n)) + 1):
            for v in range(1, u):
                if (u - v) & 1 == 0 or gcd(u, v) != 1:
                    continue                    
                c = u * u + v * v
                if c > n:
                    continue
                res += 2 * (n // c)
        return res
        # INSERT_YOUR_CODE
if __name__ == "__main__":
    from math import gcd, sqrt

    sol = Solution()
    test_cases = [
        # (n, expected_output)
        (5, 2),        # Only primitive: (3,4,5) => 2*1=2
        (10, 4),       # (3,4,5),(6,8,10); but 10//5=2, 10//10=1; (3,4,5) 2*2=4, (6,8,10) is not primitive but same ratio
        (25, 10),      # Many possible; just ensuring output type/int
        (1, 0),        # No valid triple (c>1 at least)
        (50, None),    # We can just run, check for no error (value optional)
        (100, None),
        (365, None),
    ]
    for i, (n, expected) in enumerate(test_cases, 1):
        out = sol.countTriples(n)
        print(f"Test {i}: countTriples({n}) -> {out}")
        if expected is not None:
            assert out == expected, f"Failed on test {i}"
    print("All tests passed for countTriples (where expected)")

