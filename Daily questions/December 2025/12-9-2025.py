class Solution:
    MOD = 10**9 + 7

    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        first = complexity[0]

        for i in range(1, n):
            if complexity[i] <= first:
                return 0

        fact = 1
        for i in range(2, n):
            fact = (fact * i) % self.MOD

        return fact

if __name__ == "__main__":
    from typing import List

    sol = Solution()
    test_cases = [
        # (complexity, expected_output)
        ([1,2,3], 2),               # 2 = (n-1)! for n=3
        ([5,6,7,8], 6),             # 6 = 3! for n=4
        ([2,1,3], 0),               # fails increasing order after first
        ([1], 1),                   # single item: vacuously one way (0! = 1)
        ([1,3,2], 0),               # fails increasing
        ([10,20,21,22,50], 24),     # 4! = 24 for n=5
        ([5,6,3,8], 0),             # fails increasing order after first
        ([2,3], 1),                 # 1! = 1 for n=2
    ]
    for i, (complexity, expected) in enumerate(test_cases, 1):
        out = sol.countPermutations(complexity)
        print(f"Test {i}: countPermutations({complexity}) -> {out}")
        assert out == expected, f"Failed on test {i}"
    print("All tests passed for countPermutations")