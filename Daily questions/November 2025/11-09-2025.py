class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def f(x, y, cnt):
            if x==0 or y==0: return cnt
        #    if x<y: return f(y, x, cnt)
            q,r=divmod(x, y)
            return f(y, r, cnt+q)
        return f(num1, num2, 0)


# Simple tests consistent with repository style (print + assert)
def test_countOperations():
    solver = Solution()

    # Test 1: Both numbers are zero
    num1_1, num2_1 = 0, 0
    res1 = solver.countOperations(num1_1, num2_1)
    print("Test 1: num1=", num1_1, "num2=", num2_1, "->", res1)
    assert res1 == 0

    # Test 2: One number is zero
    num1_2, num2_2 = 5, 0
    res2 = solver.countOperations(num1_2, num2_2)
    print("Test 2: num1=", num1_2, "num2=", num2_2, "->", res2)
    assert res2 == 0

    # Test 3: Basic case - num1 > num2
    num1_3, num2_3 = 2, 3
    res3 = solver.countOperations(num1_3, num2_3)
    print("Test 3: num1=", num1_3, "num2=", num2_3, "->", res3)
    assert res3 == 3

    # Test 4: Equal numbers
    num1_4, num2_4 = 5, 5
    res4 = solver.countOperations(num1_4, num2_4)
    print("Test 4: num1=", num1_4, "num2=", num2_4, "->", res4)
    assert res4 == 1

    # Test 5: num1 is multiple of num2
    num1_5, num2_5 = 10, 5
    res5 = solver.countOperations(num1_5, num2_5)
    print("Test 5: num1=", num1_5, "num2=", num2_5, "->", res5)
    assert res5 == 1

    # Test 6: num2 is multiple of num1
    num1_6, num2_6 = 3, 9
    res6 = solver.countOperations(num1_6, num2_6)
    print("Test 6: num1=", num1_6, "num2=", num2_6, "->", res6)
    assert res6 == 3

    # Test 7: Larger numbers
    num1_7, num2_7 = 13, 5
    res7 = solver.countOperations(num1_7, num2_7)
    print("Test 7: num1=", num1_7, "num2=", num2_7, "->", res7)
    assert res7 == 6

    # Test 8: Small numbers
    num1_8, num2_8 = 1, 1
    res8 = solver.countOperations(num1_8, num2_8)
    print("Test 8: num1=", num1_8, "num2=", num2_8, "->", res8)
    assert res8 == 1

    # Test 9: One is 1
    num1_9, num2_9 = 1, 10
    res9 = solver.countOperations(num1_9, num2_9)
    print("Test 9: num1=", num1_9, "num2=", num2_9, "->", res9)
    assert res9 == 10

    # Test 10: Larger test case
    num1_10, num2_10 = 20, 7
    res10 = solver.countOperations(num1_10, num2_10)
    print("Test 10: num1=", num1_10, "num2=", num2_10, "->", res10)
    assert res10 == 9

    print("All tests passed!")


if __name__ == "__main__":
    test_countOperations()