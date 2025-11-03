from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        l=0
        removes=0
        for r in range(n):
            if (colors[r]!=colors[l]):
                sameColors=neededTime[l:r]
                removes+=sum(sameColors)-max(sameColors)
                l=r
        removes+=sum(neededTime[l:])-max(neededTime[l:])
        return removes


# Simple tests consistent with repository style (print + assert)
def test_minCost():
    solver = Solution()

    # Test 1: No removals needed (no consecutive same colors)
    colors1, time1 = "aba", [1, 2, 3]
    res1 = solver.minCost(colors1, time1)
    print("Test 1:", colors1, time1, "->", res1)
    assert res1 == 0

    # Test 2: Two groups of same colors
    colors2, time2 = "aaabbb", [1, 2, 3, 4, 5, 6]
    res2 = solver.minCost(colors2, time2)
    print("Test 2:", colors2, time2, "->", res2)
    assert res2 == 12

    # Test 3: Multiple separated groups
    colors3, time3 = "aabaa", [1, 2, 3, 4, 1]
    res3 = solver.minCost(colors3, time3)
    print("Test 3:", colors3, time3, "->", res3)
    assert res3 == 2

    # Test 4: Single character
    colors4, time4 = "a", [5]
    res4 = solver.minCost(colors4, time4)
    print("Test 4:", colors4, time4, "->", res4)
    assert res4 == 0

    # Test 5: All same characters
    colors5, time5 = "aaaa", [4, 3, 2, 1]
    res5 = solver.minCost(colors5, time5)
    print("Test 5:", colors5, time5, "->", res5)
    assert res5 == 6

    # Test 6: Alternating colors
    colors6, time6 = "abab", [1, 2, 3, 4]
    res6 = solver.minCost(colors6, time6)
    print("Test 6:", colors6, time6, "->", res6)
    assert res6 == 0

    # Test 7: Two same with equal times
    colors7, time7 = "aa", [5, 5]
    res7 = solver.minCost(colors7, time7)
    print("Test 7:", colors7, time7, "->", res7)
    assert res7 == 5

    # Test 8: Long group with varied times
    colors8, time8 = "bbbbba", [1, 10, 2, 9, 3, 7]
    res8 = solver.minCost(colors8, time8)
    print("Test 8:", colors8, time8, "->", res8)
    # For bbbbb: sum(1,10,2,9,3)-max(10) = 5; 'a' alone -> 0; total 5
    assert res8 == 5

    print("All tests passed!")


if __name__ == "__main__":
    test_minCost()