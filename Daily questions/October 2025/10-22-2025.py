from typing import List
from collections import Counter
from bisect import bisect_left, bisect_right


class Solution:
    def maxFrequency(self, a: List[int], k: int, op: int) -> int:
        a,z = sorted(a),Counter(a)
        return max(max(min(bisect_right(a,v+k)-bisect_left(a,v-k)-z[v],op)+z[v],
            min(bisect_right(a,v+2*k)-i,op)) for i,v in enumerate(a))


# Simple tests consistent with repository style (print + assert)
def test_maxFrequency():
    solver = Solution()

    # Test 1: Single element array
    a1, k1, op1 = [1], 1, 1
    res1 = solver.maxFrequency(a1, k1, op1)
    print("Test 1:", a1, k1, op1, "->", res1)
    assert res1 == 1

    # Test 2: Two identical elements
    a2, k2, op2 = [2, 2], 1, 1
    res2 = solver.maxFrequency(a2, k2, op2)
    print("Test 2:", a2, k2, op2, "->", res2)
    assert res2 == 2

    # Test 3: Two different elements with operations
    a3, k3, op3 = [1, 2], 1, 1
    res3 = solver.maxFrequency(a3, k3, op3)
    print("Test 3:", a3, k3, op3, "->", res3)
    assert res3 == 2

    # Test 4: Multiple elements with no operations
    a4, k4, op4 = [1, 2, 3, 4], 1, 0
    res4 = solver.maxFrequency(a4, k4, op4)
    print("Test 4:", a4, k4, op4, "->", res4)
    assert res4 == 1

    # Test 5: Multiple elements with operations
    a5, k5, op5 = [1, 2, 3, 4], 1, 2
    res5 = solver.maxFrequency(a5, k5, op5)
    print("Test 5:", a5, k5, op5, "->", res5)
    assert res5 == 3

    # Test 6: Array with duplicates
    a6, k6, op6 = [1, 1, 2, 2, 3], 1, 2
    res6 = solver.maxFrequency(a6, k6, op6)
    print("Test 6:", a6, k6, op6, "->", res6)
    assert res6 == 4

    # Test 7: Large k value
    a7, k7, op7 = [1, 2, 3], 10, 1
    res7 = solver.maxFrequency(a7, k7, op7)
    print("Test 7:", a7, k7, op7, "->", res7)
    assert res7 == 3

    # Test 8: Large op value
    a8, k8, op8 = [1, 2, 3, 4, 5], 1, 10
    res8 = solver.maxFrequency(a8, k8, op8)
    print("Test 8:", a8, k8, op8, "->", res8)
    assert res8 == 5

    # Test 9: Edge case with zero k
    a9, k9, op9 = [1, 2, 3], 0, 2
    res9 = solver.maxFrequency(a9, k9, op9)
    print("Test 9:", a9, k9, op9, "->", res9)
    assert res9 == 1

    # Test 10: Edge case with zero op
    a10, k10, op10 = [1, 2, 3], 1, 0
    res10 = solver.maxFrequency(a10, k10, op10)
    print("Test 10:", a10, k10, op10, "->", res10)
    assert res10 == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_maxFrequency()