class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import Counter
        from typing import List

        freq = Counter(p[1] for p in points)
        Sum, c2 = 0, 0
        for f in freq.values():
            if f <= 1:
                continue
            c = f * (f - 1) // 2
            Sum += c
            c2 += c * c
        return (Sum * Sum - c2) // 2 % (10**9 + 7)


# --- Simple tests consistent with repository style (print + assert) ---
def test_countTrapezoids():
    solver = Solution()

    # Test 1: No points
    points1 = []
    out1 = solver.countTrapezoids(points1)
    print("Test 1:", points1, "->", out1)
    assert out1 == 0

    # Test 2: All points with unique y
    points2 = [[0, 0], [1, 1], [2, 2]]
    out2 = solver.countTrapezoids(points2)
    print("Test 2:", points2, "->", out2)
    assert out2 == 0

    # Test 3: Two points on same y
    points3 = [[0, 1], [1, 1]]
    out3 = solver.countTrapezoids(points3)
    print("Test 3:", points3, "->", out3)
    assert out3 == 0

    # Test 4: Four points on two parallel lines (y=1 and y=2), total should be 1
    points4 = [[0, 1], [1, 1], [2, 2], [3, 2]]
    out4 = solver.countTrapezoids(points4)
    print("Test 4:", points4, "->", out4)
    assert out4 == 1

    # Test 5: Six points, three on y=1, three on y=2 (3 choose 2 = 3 each, so 9 possible trapezoids)
    points5 = [[0, 1], [1, 1], [2, 1], [3, 2], [4, 2], [5, 2]]
    out5 = solver.countTrapezoids(points5)
    print("Test 5:", points5, "->", out5)
    assert out5 == 9

    # Test 6: All points on one level (no trapezoid)
    points6 = [[1, 42], [2, 42], [3, 42], [4, 42]]
    out6 = solver.countTrapezoids(points6)
    print("Test 6:", points6, "->", out6)
    assert out6 == 0

    # Test 7: Moderate case with more than two levels
    points7 = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [0, 2], [1, 2], [2, 2]]
    out7 = solver.countTrapezoids(points7)
    print("Test 7:", points7, "->", out7)
    # For y=0: 3 points; y=1: 2 points; y=2: 3 points
    # (3 choose 2)=3, (2 choose 2)=1, (3 choose 2)=3. So total pairs: 3+1+3=7. Sum=7. c2=9+1+9=19. (49-19)//2=15
    assert out7 == 15

# Uncomment to run tests
# test_countTrapezoids()