from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if op[1] == '+' else -1 for op in operations)


# Simple tests consistent with repository style (print + assert)
def test_finalValueAfterOperations():
    solver = Solution()

    # Test 1: Empty operations -> 0
    ops1 = []
    res1 = solver.finalValueAfterOperations(ops1)
    print("Test 1:", ops1, "->", res1)
    assert res1 == 0

    # Test 2: Single increment -> 1
    ops2 = ["X++"]
    res2 = solver.finalValueAfterOperations(ops2)
    print("Test 2:", ops2, "->", res2)
    assert res2 == 1

    # Test 3: Single decrement -> -1
    ops3 = ["--X"]
    res3 = solver.finalValueAfterOperations(ops3)
    print("Test 3:", ops3, "->", res3)
    assert res3 == -1

    # Test 4: Mix with net +1
    ops4 = ["X++", "++X", "X--"]
    res4 = solver.finalValueAfterOperations(ops4)
    print("Test 4:", ops4, "->", res4)
    assert res4 == 1

    # Test 5: Mix with net 0
    ops5 = ["X++", "X--", "++X", "--X"]
    res5 = solver.finalValueAfterOperations(ops5)
    print("Test 5:", ops5, "->", res5)
    assert res5 == 0

    # Test 6: Multiple increments -> 3
    ops6 = ["++X", "X++", "++X", "X++", "--X"]
    res6 = solver.finalValueAfterOperations(ops6)
    print("Test 6:", ops6, "->", res6)
    assert res6 == 3

    print("All tests passed!")


if __name__ == "__main__":
    test_finalValueAfterOperations()