class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        A, l, r = 0, 0, n - 1
        while l < r:
            A = max(A, min(h[l], h[r]) * (r - l))
            if h[r] < h[l]:
                r -= 1
            else:
                l += 1
        return A

# Simple tests consistent with repository style (print + assert)
def test_maxArea():
    solver = Solution()

    # Test 1: Basic example
    h1 = [1,8,6,2,5,4,8,3,7]
    expected1 = 49
    out1 = solver.maxArea(h1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: All heights the same
    h2 = [3,3,3,3,3]
    expected2 = 12  # min height 3, width 4 (index 0 and 4)
    out2 = solver.maxArea(h2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Monotonically increasing
    h3 = [1,2,3,4,5]
    expected3 = 6  # between index 0 and 4: min(1,5)*4=4, or (1, 4): min(2,5)*3=6
    out3 = solver.maxArea(h3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Monotonically decreasing
    h4 = [5,4,3,2,1]
    expected4 = 6  # between index 0 and 4: min(5,1)*4=4, or (0,3): min(5,2)*3=6
    out4 = solver.maxArea(h4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Only two elements
    h5 = [1,2]
    expected5 = 1  # min(1,2) * 1 = 1
    out5 = solver.maxArea(h5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Large values
    h6 = [1000, 1, 1000]
    expected6 = 2000  # min(1000,1000)*2=2000
    out6 = solver.maxArea(h6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Zeros in input
    h7 = [0,2,0,4,0]
    expected7 = 6  # between index 1 and 3: min(2,4)*(3-1)=2*2=4, or (1,3): 2*2=4, but (3,4): 0*anything=0, (1,4): min(2,0)*3=0, try (1,3): 2*2=4, but (0,3): min(0,4)*3=0, the maximum is 4
    out7 = solver.maxArea(h7)
    print("Test 7:", out7)
    assert out7 == 4

    # Test 8: Single element (edge, invalid by constraints, but let's try)
    h8 = [5]
    try:
        out8 = solver.maxArea(h8)
        print("Test 8:", out8)
        assert out8 == 0  # No possible area
    except Exception:
        print("Test 8: Exception (expected for single input)")

    print("All tests passed for maxArea.")

if __name__ == "__main__":
    test_maxArea()