class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        prev = [[0]*k for _ in range(n)]
        curr = [[0]*k for _ in range(n)]

        s = 0
        for j in range(n):
            s = (s + grid[0][j]) % k
            prev[j][s] = 1

        s = grid[0][0] % k

        for i in range(1, m):
            s = (s + grid[i][0]) % k
            curr[0] = [0]*k
            curr[0][s] = 1

            for j in range(1, n):
                curr[j] = [0]*k
                val = grid[i][j]
                for r in range(k):
                    nr = (r + val) % k
                    curr[j][nr] = (prev[j][r] + curr[j - 1][r]) % MOD

            prev, curr = curr, prev

        return prev[n - 1][0]

# Simple tests consistent with repository style (print + assert)
def test_numberOfPaths():
    solver = Solution()

    # Test 1: 2x2 grid, k=3, all 1s
    grid1 = [
        [1, 1],
        [1, 1]
    ]
    k1 = 3
    out1 = solver.numberOfPaths(grid1, k1)
    print("Test 1:", out1)
    assert out1 == 0  # Only sums are 3,4 (never mod 3 = 0)

    # Test 2: 2x2 grid, k=2, one obvious path
    grid2 = [
        [1, 1],
        [0, 1]
    ]
    k2 = 2
    out2 = solver.numberOfPaths(grid2, k2)
    print("Test 2:", out2)
    assert out2 == 1  # Only path down, right: 1+0+1=2→2%2==0

    # Test 3: 1x3 grid, k=2
    grid3 = [
        [1, 1, 1]
    ]
    k3 = 2
    out3 = solver.numberOfPaths(grid3, k3)
    print("Test 3:", out3)
    assert out3 == 1  # Sum = 3, only path right-right (3%2==1), but we start at 1 so only way with 0 mod is if k=1

    # Test 4: Larger, k = 5
    grid4 = [
        [5, 5],
        [5, 5]
    ]
    k4 = 5
    out4 = solver.numberOfPaths(grid4, k4)
    print("Test 4:", out4)
    assert out4 == 2  # Both possible paths (down,right or right,down) are 5+5+5=15, 15%5==0

    # Test 5: Single cell, k = value
    grid5 = [[7]]
    k5 = 7
    out5 = solver.numberOfPaths(grid5, k5)
    print("Test 5:", out5)
    assert out5 == 1

if __name__ == "__main__":
    from typing import List
    test_numberOfPaths()