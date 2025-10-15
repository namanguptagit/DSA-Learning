from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        length = len(heights)

        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:
                bar = stack.pop()
                pse = stack[-1] if stack else -1
                nse = i
                area = max(area, heights[bar] * (nse - pse - 1))
            stack.append(i)

        while stack:
            bar = stack.pop()
            pse = stack[-1] if stack else -1
            nse = length
            area = max(area, heights[bar] * (nse - pse - 1))

        return area

# Test cases
def test_largest_rectangle_area():
    solution = Solution()
    
    # Test Case 1: Basic cases
    print("Test Case 1: Basic histogram cases")
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([1, 2, 3, 4, 5], 9),
        ([5, 4, 3, 2, 1], 9)
    ]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 1.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 2: Single element
    print("Test Case 2: Single element")
    test_cases = [([1], 1), ([5], 5), ([0], 0)]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 2.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 3: Empty array
    print("Test Case 3: Empty array")
    result3 = solution.largestRectangleArea([])
    print(f"Input: []")
    print(f"Expected: 0, Got: {result3}")
    print(f"Test 3 {'PASSED' if result3 == 0 else 'FAILED'}\n")
    
    # Test Case 4: All same heights
    print("Test Case 4: All same heights")
    test_cases = [([3, 3, 3, 3], 12), ([2, 2, 2], 6), ([1, 1], 2)]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 4.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 5: Increasing heights
    print("Test Case 5: Increasing heights")
    test_cases = [([1, 2, 3, 4, 5], 9), ([2, 4, 6, 8], 12)]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 5.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 6: Decreasing heights
    print("Test Case 6: Decreasing heights")
    test_cases = [([5, 4, 3, 2, 1], 9), ([8, 6, 4, 2], 12)]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 6.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 7: Peak in the middle
    print("Test Case 7: Peak in the middle")
    test_cases = [
        ([1, 3, 2, 1], 4),
        ([2, 1, 2], 3),
        ([1, 4, 3, 2, 1], 6)
    ]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 7.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 8: Valley in the middle
    print("Test Case 8: Valley in the middle")
    test_cases = [
        ([3, 1, 3], 3),
        ([4, 2, 1, 2, 4], 8),
        ([5, 3, 2, 3, 5], 10)
    ]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 8.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 9: Zero heights
    print("Test Case 9: Zero heights")
    test_cases = [
        ([0, 0, 0], 0),
        ([1, 0, 2], 2),
        ([0, 3, 0], 3)
    ]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 9.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 10: Large numbers
    print("Test Case 10: Large numbers")
    test_cases = [
        ([1000000, 1, 1000000], 2000000),
        ([1000, 2000, 3000], 4000),
        ([999999, 888888, 777777], 1999998)
    ]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 10.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 11: Complex cases
    print("Test Case 11: Complex cases")
    test_cases = [
        ([6, 2, 5, 4, 5, 1, 6], 12),
        ([2, 1, 2, 3, 1], 5),
        ([1, 2, 3, 2, 1], 6)
    ]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 11.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 12: Edge case - two elements
    print("Test Case 12: Two elements")
    test_cases = [([1, 2], 2), ([2, 1], 2), ([3, 3], 6)]
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 12.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    print("🎉 All test cases completed!")

if __name__ == "__main__":
    test_largest_rectangle_area()