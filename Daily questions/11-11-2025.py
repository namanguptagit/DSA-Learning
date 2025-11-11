from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}

        for s in strs:
            ones = s.count('1')
            zeroes = s.count('0')
            newdp = {}

            for (prevZeroes, prevOnes), val in dp.items():
                newZeroes, newOnes = prevZeroes + zeroes, prevOnes + ones
                if newZeroes <= m and newOnes <= n:
                    if (newZeroes, newOnes) not in dp or dp[(newZeroes, newOnes)] < val + 1:
                        newdp[(newZeroes, newOnes)] = val + 1

            dp.update(newdp)

        return max(dp.values())


# Simple tests consistent with repository style (print + assert)
def test_findMaxForm():
    solver = Solution()

    # Test 1: Basic example
    strs1 = ["10", "0001", "111001", "1", "0"]
    m1, n1 = 5, 3
    res1 = solver.findMaxForm(strs1, m1, n1)
    print("Test 1:", strs1, "m=", m1, "n=", n1, "->", res1)
    assert res1 == 4  # pick "10","0001","1","0"

    # Test 2: Another common example
    strs2 = ["10", "0", "1"]
    m2, n2 = 1, 1
    res2 = solver.findMaxForm(strs2, m2, n2)
    print("Test 2:", strs2, "m=", m2, "n=", n2, "->", res2)
    assert res2 == 2  # pick "0" and "1"

    # Test 3: No capacity
    strs3 = ["0", "1", "01"]
    m3, n3 = 0, 0
    res3 = solver.findMaxForm(strs3, m3, n3)
    print("Test 3:", strs3, "m=", m3, "n=", n3, "->", res3)
    assert res3 == 0

    # Test 4: Only zeros allowed
    strs4 = ["0", "00", "1", "10"]
    m4, n4 = 3, 0
    res4 = solver.findMaxForm(strs4, m4, n4)
    print("Test 4:", strs4, "m=", m4, "n=", n4, "->", res4)
    assert res4 == 2  # pick "0" and "00"

    # Test 5: Only ones allowed
    strs5 = ["1", "1", "11"]
    m5, n5 = 0, 2
    res5 = solver.findMaxForm(strs5, m5, n5)
    print("Test 5:", strs5, "m=", m5, "n=", n5, "->", res5)
    assert res5 == 2  # pick "1" and "1"

    # Test 6: Larger mix (sanity)
    strs6 = ["10", "0001", "111001", "1", "0", "01", "001", "110"]
    m6, n6 = 7, 5
    res6 = solver.findMaxForm(strs6, m6, n6)
    print("Test 6:", strs6, "m=", m6, "n=", n6, "->", res6)
    assert res6 >= 4  # at least as good as baseline example

    print("All tests passed!")


if __name__ == "__main__":
    test_findMaxForm()