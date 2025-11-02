from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 2
        for r, c in walls:
            grid[r][c] = 2

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for gr, gc in guards:
            for dr, dc in dirs:
                r, c = gr + dr, gc + dc
                while 0 <= r < m and 0 <= c < n and grid[r][c] < 2:
                    grid[r][c] = 1  
                    r += dr
                    c += dc

        count = sum(cell == 0 for row in grid for cell in row)

        return count


# Simple tests consistent with repository style (print + assert)
def test_countUnguarded():
    solver = Solution()

    # Test 1: Basic case with one guard
    m1, n1, guards1, walls1 = 4, 6, [[0, 0]], [[2, 2]]
    res1 = solver.countUnguarded(m1, n1, guards1, walls1)
    print("Test 1: m={}, n={}, guards={}, walls={} -> {}".format(m1, n1, guards1, walls1, res1))
    assert res1 == 7

    # Test 2: Multiple guards
    m2, n2, guards2, walls2 = 4, 6, [[0, 0], [1, 1], [2, 4]], [[0, 2], [2, 2]]
    res2 = solver.countUnguarded(m2, n2, guards2, walls2)
    print("Test 2: m={}, n={}, guards={}, walls={} -> {}".format(m2, n2, guards2, walls2, res2))
    assert res2 == 4

    # Test 3: No guards
    m3, n3, guards3, walls3 = 3, 3, [], [[1, 1]]
    res3 = solver.countUnguarded(m3, n3, guards3, walls3)
    print("Test 3: m={}, n={}, guards={}, walls={} -> {}".format(m3, n3, guards3, walls3, res3))
    assert res3 == 8

    # Test 4: No walls
    m4, n4, guards4, walls4 = 3, 3, [[1, 1]], []
    res4 = solver.countUnguarded(m4, n4, guards4, walls4)
    print("Test 4: m={}, n={}, guards={}, walls={} -> {}".format(m4, n4, guards4, walls4, res4))
    assert res4 == 0

    # Test 5: Guard at corner
    m5, n5, guards5, walls5 = 4, 4, [[0, 0]], []
    res5 = solver.countUnguarded(m5, n5, guards5, walls5)
    print("Test 5: m={}, n={}, guards={}, walls={} -> {}".format(m5, n5, guards5, walls5, res5))
    assert res5 == 9

    # Test 6: Guard at center
    m6, n6, guards6, walls6 = 5, 5, [[2, 2]], []
    res6 = solver.countUnguarded(m6, n6, guards6, walls6)
    print("Test 6: m={}, n={}, guards={}, walls={} -> {}".format(m6, n6, guards6, walls6, res6))
    assert res6 == 12

    # Test 7: All cells guarded
    m7, n7, guards7, walls7 = 2, 2, [[0, 0], [0, 1], [1, 0], [1, 1]], []
    res7 = solver.countUnguarded(m7, n7, guards7, walls7)
    print("Test 7: m={}, n={}, guards={}, walls={} -> {}".format(m7, n7, guards7, walls7, res7))
    assert res7 == 0

    # Test 8: Single cell grid with guard
    m8, n8, guards8, walls8 = 1, 1, [[0, 0]], []
    res8 = solver.countUnguarded(m8, n8, guards8, walls8)
    print("Test 8: m={}, n={}, guards={}, walls={} -> {}".format(m8, n8, guards8, walls8, res8))
    assert res8 == 0

    # Test 9: Single cell grid with wall
    m9, n9, guards9, walls9 = 1, 1, [], [[0, 0]]
    res9 = solver.countUnguarded(m9, n9, guards9, walls9)
    print("Test 9: m={}, n={}, guards={}, walls={} -> {}".format(m9, n9, guards9, walls9, res9))
    assert res9 == 0

    # Test 10: Guards blocking each other
    m10, n10, guards10, walls10 = 3, 3, [[1, 0], [1, 2]], []
    res10 = solver.countUnguarded(m10, n10, guards10, walls10)
    print("Test 10: m={}, n={}, guards={}, walls={} -> {}".format(m10, n10, guards10, walls10, res10))
    assert res10 == 3

    # Test 11: Wall blocking guard's view
    m11, n11, guards11, walls11 = 4, 4, [[1, 1]], [[1, 2]]
    res11 = solver.countUnguarded(m11, n11, guards11, walls11)
    print("Test 11: m={}, n={}, guards={}, walls={} -> {}".format(m11, n11, guards11, walls11, res11))
    assert res11 == 10

    # Test 12: Multiple guards and walls
    m12, n12, guards12, walls12 = 5, 5, [[1, 1], [3, 3]], [[2, 2]]
    res12 = solver.countUnguarded(m12, n12, guards12, walls12)
    print("Test 12: m={}, n={}, guards={}, walls={} -> {}".format(m12, n12, guards12, walls12, res12))
    assert res12 == 12

    # Test 13: Empty grid (edge case)
    m13, n13, guards13, walls13 = 0, 0, [], []
    res13 = solver.countUnguarded(m13, n13, guards13, walls13)
    print("Test 13: m={}, n={}, guards={}, walls={} -> {}".format(m13, n13, guards13, walls13, res13))
    assert res13 == 0

    # Test 14: Guards at edges
    m14, n14, guards14, walls14 = 3, 3, [[0, 1], [1, 0], [1, 2], [2, 1]], []
    res14 = solver.countUnguarded(m14, n14, guards14, walls14)
    print("Test 14: m={}, n={}, guards={}, walls={} -> {}".format(m14, n14, guards14, walls14, res14))
    assert res14 == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_countUnguarded()