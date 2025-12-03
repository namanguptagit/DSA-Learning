from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        t = defaultdict(lambda: defaultdict(int))
        v = defaultdict(lambda: defaultdict(int))

        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                g = gcd(dx, abs(dy))
                sx = dx // g
                sy = dy // g

                des = sx * y1 - sy * x1

                key1 = (sx << 12) | (sy + 2000)
                key2 = (dx << 12) | (dy + 2000)

                t[key1][des] += 1
                v[key2][des] += 1

        return self.count(t) - self.count(v) // 2

    def count(self, mp):
        ans = 0

        for inner in mp.values():
            total = sum(inner.values())
            remaining = total

            for val in inner.values():
                remaining -= val
                ans += val * remaining

        return ans

# Test cases - added as per convention in other files
if __name__ == "__main__":
    sol = Solution()
    # Example test case 1: simple trapezoid
    points1 = [[0,0], [2,0], [1,1], [3,1]]
    print(sol.countTrapezoids(points1))  # Expected output: (depends on logic, placeholder)

    # Example test case 2: 4 points in a line (should be 0)
    points2 = [[0,0], [1,0], [2,0], [3,0]]
    print(sol.countTrapezoids(points2))  # Expected output: 0

    # Example test case 3: generic points
    points3 = [[0,0], [1,2], [2,1], [3,3], [1,1], [2,2]]
    print(sol.countTrapezoids(points3))  # Expected output: (depends on logic)

    # Example test case 4: duplicate points (should not affect count)
    points4 = [[0,0], [1,0], [1,1], [2,1], [2,0], [1,1]]
    print(sol.countTrapezoids(points4))  # Expected output: (depends on logic)