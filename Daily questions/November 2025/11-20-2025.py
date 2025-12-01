class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        ans = 0
        a, b = -1, -1

        for l, r in intervals:
            if l > b:
                a = r - 1
                b = r
                ans += 2
            elif l > a:
                a = b
                b = r
                ans += 1

        return ans

# Simple tests consistent with repository style (print + assert)
def test_intersectionSizeTwo():
    solver = Solution()

    # Test 1: Example from Leetcode
    intervals1 = [[1,3],[1,4],[2,5],[3,5]]
    expected1 = 3
    out1 = solver.intersectionSizeTwo([x[:] for x in intervals1])
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Disjoint intervals
    intervals2 = [[1,2],[3,4],[5,6]]
    expected2 = 6   # Each needs 2 elements
    out2 = solver.intersectionSizeTwo([x[:] for x in intervals2])
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: One interval
    intervals3 = [[5,10]]
    expected3 = 2
    out3 = solver.intersectionSizeTwo([x[:] for x in intervals3])
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Fully overlapping intervals
    intervals4 = [[1,5],[2,5],[3,5]]
    expected4 = 2
    out4 = solver.intersectionSizeTwo([x[:] for x in intervals4])
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Intervals with some overlap
    intervals5 = [[1,2],[2,3],[3,4],[2,5],[4,7]]
    expected5 = 5
    out5 = solver.intersectionSizeTwo([x[:] for x in intervals5])
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Large numbers, single interval
    intervals6 = [[1000,10000]]
    expected6 = 2
    out6 = solver.intersectionSizeTwo([x[:] for x in intervals6])
    print("Test 6:", out6)
    assert out6 == expected6

    print("All tests passed for intersectionSizeTwo.")

if __name__ == "__main__":
    test_intersectionSizeTwo()