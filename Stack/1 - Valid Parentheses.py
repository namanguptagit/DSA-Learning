class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in ")]}":
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        
        return not stack

# Test cases
def test_valid_parentheses():
    solution = Solution()
    
    # Test Case 1: Basic valid cases
    print("Test Case 1: Basic valid parentheses")
    test_cases = ["()", "()[]{}", "([{}])"]
    for i, test_case in enumerate(test_cases, 1):
        result = solution.isValid(test_case)
        print(f"Input: \"{test_case}\"")
        print(f"Expected: True, Got: {result}")
        print(f"Test 1.{i} {'PASSED' if result == True else 'FAILED'}\n")
    
    # Test Case 2: Basic invalid cases
    print("Test Case 2: Basic invalid parentheses")
    test_cases = ["(]", "([)]", "((("]
    for i, test_case in enumerate(test_cases, 1):
        result = solution.isValid(test_case)
        print(f"Input: \"{test_case}\"")
        print(f"Expected: False, Got: {result}")
        print(f"Test 2.{i} {'PASSED' if result == False else 'FAILED'}\n")
    
    # Test Case 3: Empty string
    print("Test Case 3: Empty string")
    result3 = solution.isValid("")
    print(f"Input: \"\"")
    print(f"Expected: True, Got: {result3}")
    print(f"Test 3 {'PASSED' if result3 == True else 'FAILED'}\n")
    
    # Test Case 4: Single character
    print("Test Case 4: Single character")
    test_cases = ["(", ")", "[", "]", "{", "}"]
    for i, test_case in enumerate(test_cases, 1):
        result = solution.isValid(test_case)
        expected = False  # Single opening or closing bracket should be invalid
        print(f"Input: \"{test_case}\"")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test 4.{i} {'PASSED' if result == expected else 'FAILED'}\n")
    
    # Test Case 5: Nested valid parentheses
    print("Test Case 5: Nested valid parentheses")
    test_cases = ["((()))", "{[()()]}", "(([]){})", "({}[])"]
    for i, test_case in enumerate(test_cases, 1):
        result = solution.isValid(test_case)
        print(f"Input: \"{test_case}\"")
        print(f"Expected: True, Got: {result}")
        print(f"Test 5.{i} {'PASSED' if result == True else 'FAILED'}\n")
    
    # Test Case 6: Mismatched brackets
    print("Test Case 6: Mismatched brackets")
    test_cases = [")(", ")]", "}{", "(()", "())", "]["]
    for i, test_case in enumerate(test_cases, 1):
        result = solution.isValid(test_case)
        print(f"Input: \"{test_case}\"")
        print(f"Expected: False, Got: {result}")
        print(f"Test 6.{i} {'PASSED' if result == False else 'FAILED'}\n")
    
    # Test Case 7: Complex valid cases
    print("Test Case 7: Complex valid cases")
    test_cases = ["{[()]}", "()[]{}", "([{}])", "((()))", "{[()()]}"]
    for i, test_case in enumerate(test_cases, 1):
        result = solution.isValid(test_case)
        print(f"Input: \"{test_case}\"")
        print(f"Expected: True, Got: {result}")
        print(f"Test 7.{i} {'PASSED' if result == True else 'FAILED'}\n")
    
    # Test Case 8: Complex invalid cases
    print("Test Case 8: Complex invalid cases")
    test_cases = ["{[()]", "()[]{}(", "([{])}", "((())", "{[()()]"]
    for i, test_case in enumerate(test_cases, 1):
        result = solution.isValid(test_case)
        print(f"Input: \"{test_case}\"")
        print(f"Expected: False, Got: {result}")
        print(f"Test 8.{i} {'PASSED' if result == False else 'FAILED'}\n")
    
    # Test Case 9: Long valid string
    print("Test Case 9: Long valid string")
    long_valid = "(" * 50 + ")" * 50
    result9 = solution.isValid(long_valid)
    print(f"Input: \"{long_valid[:20]}...{long_valid[-20:]}\" (length: {len(long_valid)})")
    print(f"Expected: True, Got: {result9}")
    print(f"Test 9 {'PASSED' if result9 == True else 'FAILED'}\n")
    
    # Test Case 10: Mixed brackets with spaces (should be invalid due to spaces)
    print("Test Case 10: Mixed brackets with spaces")
    test_cases = ["( )", "[ ]", "{ }", "( [ ) ]"]
    for i, test_case in enumerate(test_cases, 1):
        result = solution.isValid(test_case)
        print(f"Input: \"{test_case}\"")
        print(f"Expected: False, Got: {result}")
        print(f"Test 10.{i} {'PASSED' if result == False else 'FAILED'}\n")
    
    print("🎉 All test cases completed!")

if __name__ == "__main__":
    test_valid_parentheses()