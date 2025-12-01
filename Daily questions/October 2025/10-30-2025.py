from typing import List


class Solution:
    def minNumberOperations(self, t: List[int]) -> int:
        return t[0]+sum(max(x-y, 0) for x, y in zip(t[1:], t))


# Simple tests consistent with repository style (print + assert)
def test_minNumberOperations():
    solver = Solution()

    # Test 1: Single element
    t1 = [5]
    res1 = solver.minNumberOperations(t1)
    print("Test 1:", t1, "->", res1)
    assert res1 == 5

    # Test 2: Monotonically increasing
    t2 = [1, 2, 3, 4, 5]
    res2 = solver.minNumberOperations(t2)
    print("Test 2:", t2, "->", res2)
    assert res2 == 5

    # Test 3: Monotonically decreasing
    t3 = [5, 4, 3, 2, 1]
    res3 = solver.minNumberOperations(t3)
    print("Test 3:", t3, "->", res3)
    assert res3 == 5

    # Test 4: All zeros
    t4 = [0, 0, 0, 0]
    res4 = solver.minNumberOperations(t4)
    print("Test 4:", t4, "->", res4)
    assert res4 == 0

    # Test 5: Mixed case
    t5 = [1, 3, 2, 1, 2]
    res5 = solver.minNumberOperations(t5)
    print("Test 5:", t5, "->", res5)
    assert res5 == 3

    # Test 6: Peaks and valleys
    t6 = [1, 4, 2, 5, 1]
    res6 = solver.minNumberOperations(t6)
    print("Test 6:", t6, "->", res6)
    assert res6 == 8

    # Test 7: Plateau
    t7 = [2, 2, 2, 2]
    res7 = solver.minNumberOperations(t7)
    print("Test 7:", t7, "->", res7)
    assert res7 == 2

    # Test 8: Step up, step down
    t8 = [1, 3, 1, 3, 1]
    res8 = solver.minNumberOperations(t8)
    print("Test 8:", t8, "->", res8)
    assert res8 == 5

    # Test 9: Edge case empty
    t9 = []
    try:
        res9 = solver.minNumberOperations(t9)
        print("Test 9:", t9, "->", res9)
        assert False, "Should raise index error for empty list"
    except Exception as e:
        print("Test 9: Empty list -> Exception as expected:", type(e).__name__)

    # Test 10: Large numbers
    t10 = [100000, 200000, 100000]
    res10 = solver.minNumberOperations(t10)
    print("Test 10:", t10, "->", res10)
    assert res10 == 200000

    print("All tests passed!")


if __name__ == "__main__":
    test_minNumberOperations()