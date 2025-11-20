class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        currentAltitude = 0
        
        for g in gain:
            currentAltitude += g
            maxAltitude = max(maxAltitude, currentAltitude)
        
        return maxAltitude

# Simple tests consistent with repository style (print + assert)
def test_largestAltitude():
    solver = Solution()
    
    # Test 1: Example from Leetcode
    gain1 = [-5,1,5,0,-7]
    expected1 = 1 + 5   # 0, -5, -4, 1, 1, -6 -> max is 1
    out1 = solver.largestAltitude(gain1)
    print("Test 1:", out1)
    assert out1 == 1

    # Test 2: All negative gains
    gain2 = [-4,-3,-2,-1, -10]
    expected2 = 0
    out2 = solver.largestAltitude(gain2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: All positive gains
    gain3 = [3,3,3,3]
    expected3 = 0+3+3+3+3 # 0,3,6,9,12 -> max is 12
    out3 = solver.largestAltitude(gain3)
    print("Test 3:", out3)
    assert out3 == 12

    # Test 4: Mixed, max at the start
    gain4 = [10,-10,0,-5,2]
    # altitudes: 0,10,0,0,-5,-3
    out4 = solver.largestAltitude(gain4)
    print("Test 4:", out4)
    assert out4 == 10

    # Test 5: gain is empty
    gain5 = []
    out5 = solver.largestAltitude(gain5)
    print("Test 5:", out5)
    assert out5 == 0

    # Test 6: max is at the "starting" altitude (always returns 0)
    gain6 = [-1, -2, -3]
    out6 = solver.largestAltitude(gain6)
    print("Test 6:", out6)
    assert out6 == 0

    print("All tests passed for largestAltitude.")

if __name__ == "__main__":
    test_largestAltitude()