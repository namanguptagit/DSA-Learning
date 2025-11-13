from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ans = [None] * len(candies)
        for i in range(0,len(candies)):
            if candies[i]+extraCandies >= m :
                ans[i] = True
            else:
                ans[i] = False
        return ans


# Simple tests consistent with repository style (print + assert)
def test_kidsWithCandies():
    solver = Solution()

    # Test 1: Basic example
    candies1 = [2, 3, 5, 1, 3]
    extraCandies1 = 3
    res1 = solver.kidsWithCandies(candies1, extraCandies1)
    print("Test 1: candies =", candies1, "extraCandies =", extraCandies1, "->", res1)
    assert res1 == [True, True, True, False, True]

    # Test 2: All kids can have greatest
    candies2 = [4, 2, 1, 1, 2]
    extraCandies2 = 1
    res2 = solver.kidsWithCandies(candies2, extraCandies2)
    print("Test 2: candies =", candies2, "extraCandies =", extraCandies2, "->", res2)
    assert res2 == [True, False, False, False, False]

    # Test 3: Single kid
    candies3 = [5]
    extraCandies3 = 0
    res3 = solver.kidsWithCandies(candies3, extraCandies3)
    print("Test 3: candies =", candies3, "extraCandies =", extraCandies3, "->", res3)
    assert res3 == [True]

    # Test 4: Large extraCandies
    candies4 = [1, 2, 3]
    extraCandies4 = 10
    res4 = solver.kidsWithCandies(candies4, extraCandies4)
    print("Test 4: candies =", candies4, "extraCandies =", extraCandies4, "->", res4)
    assert res4 == [True, True, True]

    # Test 5: Zero extraCandies
    candies5 = [3, 1, 2]
    extraCandies5 = 0
    res5 = solver.kidsWithCandies(candies5, extraCandies5)
    print("Test 5: candies =", candies5, "extraCandies =", extraCandies5, "->", res5)
    assert res5 == [True, False, False]

    # Test 6: All same candies
    candies6 = [5, 5, 5, 5]
    extraCandies6 = 2
    res6 = solver.kidsWithCandies(candies6, extraCandies6)
    print("Test 6: candies =", candies6, "extraCandies =", extraCandies6, "->", res6)
    assert res6 == [True, True, True, True]

    # Test 7: Only one can have greatest
    candies7 = [1, 1, 1, 5]
    extraCandies7 = 1
    res7 = solver.kidsWithCandies(candies7, extraCandies7)
    print("Test 7: candies =", candies7, "extraCandies =", extraCandies7, "->", res7)
    assert res7 == [False, False, False, True]

    # Test 8: LeetCode example
    candies8 = [12, 1, 12]
    extraCandies8 = 10
    res8 = solver.kidsWithCandies(candies8, extraCandies8)
    print("Test 8: candies =", candies8, "extraCandies =", extraCandies8, "->", res8)
    assert res8 == [True, False, True]

    # Test 9: Large numbers
    candies9 = [10, 20, 15, 25]
    extraCandies9 = 5
    res9 = solver.kidsWithCandies(candies9, extraCandies9)
    print("Test 9: candies =", candies9, "extraCandies =", extraCandies9, "->", res9)
    assert res9 == [False, True, False, True]

    # Test 10: Small difference
    candies10 = [1, 2, 3, 4, 5]
    extraCandies10 = 1
    res10 = solver.kidsWithCandies(candies10, extraCandies10)
    print("Test 10: candies =", candies10, "extraCandies =", extraCandies10, "->", res10)
    assert res10 == [False, False, True, True, True]

    print("All tests passed!")


if __name__ == "__main__":
    test_kidsWithCandies()