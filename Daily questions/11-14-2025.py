class Solution:
    def rangeAddQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for row1, col1, row2, col2 in queries:
            diff[row1][col1] += 1
            diff[row2 + 1][col1] -= 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col2 + 1] += 1

        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                x1 = 0 if i == 0 else mat[i - 1][j]
                x2 = 0 if j == 0 else mat[i][j - 1]
                x3 = 0 if i == 0 or j == 0 else mat[i - 1][j - 1]
                mat[i][j] = diff[i][j] + x1 + x2 - x3
        return mat

# Simple tests consistent with repository style (print + assert)
def test_rangeAddQueries():
    solver = Solution()

    # Test 1: Simple single query, 2x2 top-left
    n1 = 3
    queries1 = [[0, 0, 1, 1]]
    expected1 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    res1 = solver.rangeAddQueries(n1, queries1)
    print("Test 1:", res1)
    assert res1 == expected1

    # Test 2: Overlapping queries on 3x3
    n2 = 3
    queries2 = [[0, 0, 1, 1], [1, 1, 2, 2]]
    expected2 = [
        [1, 1, 0],
        [1, 2, 1],
        [0, 1, 1]
    ]
    res2 = solver.rangeAddQueries(n2, queries2)
    print("Test 2:", res2)
    assert res2 == expected2

    # Test 3: Full grid
    n3 = 2
    queries3 = [[0, 0, 1, 1]]
    expected3 = [
        [1, 1],
        [1, 1]
    ]
    res3 = solver.rangeAddQueries(n3, queries3)
    print("Test 3:", res3)
    assert res3 == expected3

    # Test 4: No queries
    n4 = 4
    queries4 = []
    expected4 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    res4 = solver.rangeAddQueries(n4, queries4)
    print("Test 4:", res4)
    assert res4 == expected4

    # Test 5: Single cell update
    n5 = 4
    queries5 = [[2, 2, 2, 2]]
    expected5 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    res5 = solver.rangeAddQueries(n5, queries5)
    print("Test 5:", res5)
    assert res5 == expected5

    # Test 6: Multiple updates to same cell
    n6 = 2
    queries6 = [[0, 0, 0, 0], [0, 0, 0, 0]]
    expected6 = [
        [2, 0],
        [0, 0],
    ]
    res6 = solver.rangeAddQueries(n6, queries6)
    print("Test 6:", res6)
    assert res6 == expected6

    # Test 7: Large n, empty queries
    n7 = 5
    queries7 = []
    expected7 = [[0]*n7 for _ in range(n7)]
    res7 = solver.rangeAddQueries(n7, queries7)
    print("Test 7:", res7)
    assert res7 == expected7

    print("All tests passed for rangeAddQueries.")

if __name__ == "__main__":
    test_rangeAddQueries()