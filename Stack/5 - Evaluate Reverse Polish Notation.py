from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # division
                    # use int() to truncate toward zero (LeetCode requires this)
                    stack.append(int(a / b))

        return stack[0]


# Simple tests consistent with repository style (print + assert)
def test_evalRPN():
    solver = Solution()

    # Test 1: Basic addition
    tokens1 = ["2", "1", "+", "3", "*"]
    res1 = solver.evalRPN(tokens1)
    print("Test 1:", tokens1, "->", res1)
    assert res1 == 9  # ((2 + 1) * 3) = 9

    # Test 2: Basic subtraction and division
    tokens2 = ["4", "13", "5", "/", "+"]
    res2 = solver.evalRPN(tokens2)
    print("Test 2:", tokens2, "->", res2)
    assert res2 == 6  # (4 + (13 / 5)) = 4 + 2 = 6

    # Test 3: Complex expression
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    res3 = solver.evalRPN(tokens3)
    print("Test 3:", tokens3, "->", res3)
    assert res3 == 22

    # Test 4: Single number
    tokens4 = ["42"]
    res4 = solver.evalRPN(tokens4)
    print("Test 4:", tokens4, "->", res4)
    assert res4 == 42

    # Test 5: Simple addition
    tokens5 = ["2", "3", "+"]
    res5 = solver.evalRPN(tokens5)
    print("Test 5:", tokens5, "->", res5)
    assert res5 == 5

    # Test 6: Simple subtraction
    tokens6 = ["5", "3", "-"]
    res6 = solver.evalRPN(tokens6)
    print("Test 6:", tokens6, "->", res6)
    assert res6 == 2

    # Test 7: Simple multiplication
    tokens7 = ["4", "3", "*"]
    res7 = solver.evalRPN(tokens7)
    print("Test 7:", tokens7, "->", res7)
    assert res7 == 12

    # Test 8: Division with truncation
    tokens8 = ["7", "2", "/"]
    res8 = solver.evalRPN(tokens8)
    print("Test 8:", tokens8, "->", res8)
    assert res8 == 3  # 7 / 2 = 3.5, truncated to 3

    # Test 9: Negative division
    tokens9 = ["-7", "2", "/"]
    res9 = solver.evalRPN(tokens9)
    print("Test 9:", tokens9, "->", res9)
    assert res9 == -3  # -7 / 2 = -3.5, truncated to -3

    # Test 10: Multiple operations
    tokens10 = ["1", "2", "+", "3", "4", "+", "*"]
    res10 = solver.evalRPN(tokens10)
    print("Test 10:", tokens10, "->", res10)
    assert res10 == 21  # ((1 + 2) * (3 + 4)) = 3 * 7 = 21

    # Test 11: Negative numbers
    tokens11 = ["-2", "3", "+"]
    res11 = solver.evalRPN(tokens11)
    print("Test 11:", tokens11, "->", res11)
    assert res11 == 1  # -2 + 3 = 1

    # Test 12: Division with negative result
    tokens12 = ["13", "5", "/"]
    res12 = solver.evalRPN(tokens12)
    print("Test 12:", tokens12, "->", res12)
    assert res12 == 2  # 13 / 5 = 2.6, truncated to 2

    print("All tests passed!")


if __name__ == "__main__":
    test_evalRPN()