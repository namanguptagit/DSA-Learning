from typing import List
from collections import Counter
class Solution:                                
    def equalPairs(self, grid: List[List[int]]) -> int:

        tpse = Counter(zip(*grid))                  # <-- determine the transpose
                                                    #     and hash the rows

        grid = Counter(map(tuple,grid))             # <-- hash the rows of grid. (Note the tuple-map, so
                                                    #     we can compare apples w/ apples in next step.)

        return  sum(tpse[t]*grid[t] for t in tpse)  # <-- compute the number of identical pairs
        # INSERT_YOUR_CODE
# Simple tests consistent with repository style (print + assert)
def test_equalPairs():
    solver = Solution()

    # Test 1: Example from LeetCode
    grid1 = [
        [3,2,1],
        [1,7,6],
        [2,7,7]
    ]
    expected1 = 1
    out1 = solver.equalPairs(grid1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Multiple pairs
    grid2 = [
        [3,1,2,2],
        [1,4,4,5],
        [2,4,2,2],
        [2,4,2,2]
    ]
    expected2 = 3  # As per LeetCode example 2
    out2 = solver.equalPairs(grid2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: No pairs
    grid3 = [
        [1,2],
        [2,1]
    ]
    expected3 = 0
    out3 = solver.equalPairs(grid3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: All rows and columns same (n x n grid of 1s)
    grid4 = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
    expected4 = 9  # 3 rows == 3 columns => 3*3 matches
    out4 = solver.equalPairs(grid4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Grid with distinct rows and columns
    grid5 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    expected5 = 0
    out5 = solver.equalPairs(grid5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: 1x1 grid
    grid6 = [
        [42],
    ]
    expected6 = 1
    out6 = solver.equalPairs(grid6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: 2x2, all elements same
    grid7 = [
        [7,7],
        [7,7]
    ]
    expected7 = 4
    out7 = solver.equalPairs(grid7)
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for equalPairs.")

if __name__ == "__main__":
    # Needed for List[List[int]], Counter
    # from typing import List
    # from collections import Counter
    test_equalPairs()