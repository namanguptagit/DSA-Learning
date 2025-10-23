from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water


# Simple tests consistent with repository style (print + assert)
def test_trap():
    solver = Solution()

    # Test 1: Empty array
    height1 = []
    res1 = solver.trap(height1)
    print("Test 1:", height1, "->", res1)
    assert res1 == 0

    # Test 2: Single element
    height2 = [1]
    res2 = solver.trap(height2)
    print("Test 2:", height2, "->", res2)
    assert res2 == 0

    # Test 3: Two elements
    height3 = [1, 2]
    res3 = solver.trap(height3)
    print("Test 3:", height3, "->", res3)
    assert res3 == 0

    # Test 4: Classic example
    height4 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res4 = solver.trap(height4)
    print("Test 4:", height4, "->", res4)
    assert res4 == 6

    # Test 5: All increasing
    height5 = [1, 2, 3, 4, 5]
    res5 = solver.trap(height5)
    print("Test 5:", height5, "->", res5)
    assert res5 == 0

    # Test 6: All decreasing
    height6 = [5, 4, 3, 2, 1]
    res6 = solver.trap(height6)
    print("Test 6:", height6, "->", res6)
    assert res6 == 0

    # Test 7: Flat array
    height7 = [3, 3, 3, 3, 3]
    res7 = solver.trap(height7)
    print("Test 7:", height7, "->", res7)
    assert res7 == 0

    # Test 8: Simple valley
    height8 = [3, 0, 2, 0, 4]
    res8 = solver.trap(height8)
    print("Test 8:", height8, "->", res8)
    assert res8 == 7

    # Test 9: Two peaks
    height9 = [2, 0, 2]
    res9 = solver.trap(height9)
    print("Test 9:", height9, "->", res9)
    assert res9 == 2

    # Test 10: Edge case with zeros
    height10 = [0, 0, 0]
    res10 = solver.trap(height10)
    print("Test 10:", height10, "->", res10)
    assert res10 == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_trap()