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


def run_tests():
    solver = Solution()

    # Valid cases
    assert solver.isValid("") is True
    assert solver.isValid("()") is True
    assert solver.isValid("()[]{}") is True
    assert solver.isValid("{[]}") is True
    assert solver.isValid("((()))") is True
    assert solver.isValid("{[()()]}") is True
    assert solver.isValid("(([]){})") is True
    assert solver.isValid("({}[])") is True

    # Invalid cases
    assert solver.isValid("(]") is False
    assert solver.isValid("([)]") is False
    assert solver.isValid("((((") is False
    assert solver.isValid(")(") is False
    assert solver.isValid(")]") is False
    assert solver.isValid("}{") is False
    assert solver.isValid("(()") is False
    assert solver.isValid("())") is False
    assert solver.isValid("][") is False

    print("All test cases passed for Valid Parentheses.")


if __name__ == "__main__":
    run_tests()