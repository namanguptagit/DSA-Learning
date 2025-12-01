class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        totalEnergy = sum(batteries)
        batteries.sort()

        for i in range(len(batteries) - 1, -1, -1):
            if batteries[i] > totalEnergy // n:
                totalEnergy -= batteries[i]
                n -= 1
            else:
                break

        return totalEnergy // n

# ---- Simple tests consistent with repository style (print + assert) ----
from typing import List

def test_maxRunTime():
    solver = Solution()
    # Test 1: LeetCode example, n = 2, batteries = [3,3,3]
    n1, batteries1 = 2, [3,3,3]
    out1 = solver.maxRunTime(n1, batteries1)
    print("Test 1:", n1, batteries1, "->", out1)
    assert out1 == 4

    # Test 2: n > len(batteries)
    n2, batteries2 = 4, [1,1,1,1]
    out2 = solver.maxRunTime(n2, batteries2)
    print("Test 2:", n2, batteries2, "->", out2)
    assert out2 == 1

    # Test 3: Some batteries too large for even distribution
    n3, batteries3 = 2, [1,2,3,100]
    out3 = solver.maxRunTime(n3, batteries3)
    print("Test 3:", n3, batteries3, "->", out3)
    assert out3 == 6

    # Test 4: Only one computer
    n4, batteries4 = 1, [100, 200, 300]
    out4 = solver.maxRunTime(n4, batteries4)
    print("Test 4:", n4, batteries4, "->", out4)
    assert out4 == 600

    # Test 5: All batteries equal, n divides totalEnergy
    n5, batteries5 = 3, [6,6,6,6]
    out5 = solver.maxRunTime(n5, batteries5)
    print("Test 5:", n5, batteries5, "->", out5)
    assert out5 == 8

    # Test 6: All batteries are 1, more computers than batteries
    n6, batteries6 = 5, [1,1,1,1,1]
    out6 = solver.maxRunTime(n6, batteries6)
    print("Test 6:", n6, batteries6, "->", out6)
    assert out6 == 1

# Uncomment to run tests
# test_maxRunTime()