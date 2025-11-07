from typing import List
from itertools import accumulate


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        df = [0] * (n + 5)
        for i, j in enumerate(stations):
            df[max(0, i - r)] += j
            df[min(n - 1, i + r) + 1] -= j
        lo, hi = min(accumulate(df[:n])), 2 * 10 ** 10
        def check(mid):
            diff = df[:]
            cur, cnt = 0, 0
            for i in range(n):
                cur += diff[i]
                if cur < mid:
                    cnt += mid - cur
                    diff[min(n - 1, i + 2 * r) + 1] -= mid - cur
                    cur = mid
                if cnt > k: return False
            return True
    
        while lo < hi:
            mid = lo + hi + 1 >> 1
            if check(mid): lo = mid
            else: hi = mid - 1
        return lo


# Simple tests consistent with repository style (print + assert)
def test_maxPower():
    solver = Solution()

    # Test 1: Basic case with small stations
    stations1, r1, k1 = [1, 2, 4, 5, 0], 1, 2
    res1 = solver.maxPower(stations1, r1, k1)
    print("Test 1: stations=", stations1, "r=", r1, "k=", k1, "->", res1)
    assert res1 == 5

    # Test 2: Single station
    stations2, r2, k2 = [4], 0, 3
    res2 = solver.maxPower(stations2, r2, k2)
    print("Test 2: stations=", stations2, "r=", r2, "k=", k2, "->", res2)
    assert res2 == 7

    # Test 3: All zeros, need to add stations
    stations3, r3, k3 = [0, 0, 0, 0], 1, 1
    res3 = solver.maxPower(stations3, r3, k3)
    print("Test 3: stations=", stations3, "r=", r3, "k=", k3, "->", res3)
    assert res3 >= 0

    # Test 4: Already high power, no additions needed
    stations4, r4, k4 = [10, 10, 10], 1, 0
    res4 = solver.maxPower(stations4, r4, k4)
    print("Test 4: stations=", stations4, "r=", r4, "k=", k4, "->", res4)
    assert res4 >= 10

    # Test 5: Large range, multiple stations
    stations5, r5, k5 = [1, 0, 0, 0, 1], 2, 2
    res5 = solver.maxPower(stations5, r5, k5)
    print("Test 5: stations=", stations5, "r=", r5, "k=", k5, "->", res5)
    assert res5 >= 0

    # Test 6: Uneven distribution
    stations6, r6, k6 = [4, 0, 0, 0, 4], 1, 1
    res6 = solver.maxPower(stations6, r6, k6)
    print("Test 6: stations=", stations6, "r=", r6, "k=", k6, "->", res6)
    assert res6 >= 0

    # Test 7: Large k value
    stations7, r7, k7 = [1, 2, 3], 1, 10
    res7 = solver.maxPower(stations7, r7, k7)
    print("Test 7: stations=", stations7, "r=", r7, "k=", k7, "->", res7)
    assert res7 >= 3

    print("All tests passed!")


if __name__ == "__main__":
    test_maxPower()