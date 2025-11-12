from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        curr = 1

        for num in target:
            # Push and Pop until we reach the current target number
            while curr < num:
                res.append("Push")
                res.append("Pop")
                curr += 1

            # Push the current target number
            res.append("Push")
            curr += 1

        return res


# Simple tests consistent with repository style (print + assert)
def test_buildArray():
    solver = Solution()

    # Test 1: Basic example
    target1 = [1, 3]
    n1 = 3
    res1 = solver.buildArray(target1, n1)
    print("Test 1: target =", target1, "n =", n1, "->", res1)
    assert res1 == ["Push", "Push", "Pop", "Push"]

    # Test 2: Sequential numbers
    target2 = [1, 2, 3]
    n2 = 3
    res2 = solver.buildArray(target2, n2)
    print("Test 2: target =", target2, "n =", n2, "->", res2)
    assert res2 == ["Push", "Push", "Push"]

    # Test 3: Single element
    target3 = [1]
    n3 = 1
    res3 = solver.buildArray(target3, n3)
    print("Test 3: target =", target3, "n =", n3, "->", res3)
    assert res3 == ["Push"]

    # Test 4: Single element not at start
    target4 = [2]
    n4 = 4
    res4 = solver.buildArray(target4, n4)
    print("Test 4: target =", target4, "n =", n4, "->", res4)
    assert res4 == ["Push", "Pop", "Push"]

    # Test 5: Gaps in sequence
    target5 = [1, 2]
    n5 = 4
    res5 = solver.buildArray(target5, n5)
    print("Test 5: target =", target5, "n =", n5, "->", res5)
    assert res5 == ["Push", "Push"]

    # Test 6: Larger gaps
    target6 = [2, 3, 4]
    n6 = 4
    res6 = solver.buildArray(target6, n6)
    print("Test 6: target =", target6, "n =", n6, "->", res6)
    assert res6 == ["Push", "Pop", "Push", "Push", "Push"]

    # Test 7: Non-consecutive
    target7 = [1, 3, 5]
    n7 = 7
    res7 = solver.buildArray(target7, n7)
    print("Test 7: target =", target7, "n =", n7, "->", res7)
    assert res7 == ["Push", "Push", "Pop", "Push", "Push", "Pop", "Push"]

    # Test 8: All numbers from 1 to n
    target8 = [1, 2, 3, 4, 5]
    n8 = 5
    res8 = solver.buildArray(target8, n8)
    print("Test 8: target =", target8, "n =", n8, "->", res8)
    assert res8 == ["Push", "Push", "Push", "Push", "Push"]

    # Test 9: Only last number
    target9 = [5]
    n9 = 5
    res9 = solver.buildArray(target9, n9)
    print("Test 9: target =", target9, "n =", n9, "->", res9)
    assert res9 == ["Push", "Pop", "Push", "Pop", "Push", "Pop", "Push", "Pop", "Push"]

    # Test 10: Multiple gaps
    target10 = [1, 4, 6]
    n10 = 7
    res10 = solver.buildArray(target10, n10)
    print("Test 10: target =", target10, "n =", n10, "->", res10)
    assert res10 == ["Push", "Push", "Pop", "Push", "Pop", "Push", "Pop", "Push", "Push", "Pop", "Push"]

    print("All tests passed!")


if __name__ == "__main__":
    test_buildArray()