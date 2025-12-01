class Solution:
    def triSum(self, n: int) -> int:
        return (n * (n + 1)) >> 1

    def totalMoney(self, days: int) -> int:
        nWeeks, rDays = divmod(days, 7)        
        return self.triSum(days) - 42 * self.triSum(nWeeks - 1) - 6 * nWeeks * rDays


# Simple tests consistent with repository style (print + assert)
def test_totalMoney():
    solver = Solution()

    # Test 1: Single day
    days1 = 1
    res1 = solver.totalMoney(days1)
    print("Test 1:", days1, "->", res1)
    assert res1 == 1

    # Test 2: One week (7 days)
    days2 = 7
    res2 = solver.totalMoney(days2)
    print("Test 2:", days2, "->", res2)
    assert res2 == 28  # 1+2+3+4+5+6+7 = 28

    # Test 3: Two weeks (14 days)
    days3 = 14
    res3 = solver.totalMoney(days3)
    print("Test 3:", days3, "->", res3)
    assert res3 == 70  # Week 1: 1+2+3+4+5+6+7=28, Week 2: 2+3+4+5+6+7+8=35, Total=63

    # Test 4: Less than a week
    days4 = 4
    res4 = solver.totalMoney(days4)
    print("Test 4:", days4, "->", res4)
    assert res4 == 10  # 1+2+3+4 = 10

    # Test 5: One week and some days
    days5 = 10
    res5 = solver.totalMoney(days5)
    print("Test 5:", days5, "->", res5)
    assert res5 == 37  # Week 1: 1+2+3+4+5+6+7=28, Week 2: 2+3+4=9, Total=37

    # Test 6: Three weeks
    days6 = 21
    res6 = solver.totalMoney(days6)
    print("Test 6:", days6, "->", res6)
    assert res6 == 96  # Week 1: 28, Week 2: 35, Week 3: 42, Total=105

    # Test 7: Edge case - zero days
    days7 = 0
    res7 = solver.totalMoney(days7)
    print("Test 7:", days7, "->", res7)
    assert res7 == 0

    # Test 8: Large number of days
    days8 = 20
    res8 = solver.totalMoney(days8)
    print("Test 8:", days8, "->", res8)
    assert res8 == 96  # 2 weeks + 6 days

    # Test 9: Exactly 8 days
    days9 = 8
    res9 = solver.totalMoney(days9)
    print("Test 9:", days9, "->", res9)
    assert res9 == 30  # Week 1: 28, Day 8: 2, Total=30

    # Test 10: Six days
    days10 = 6
    res10 = solver.totalMoney(days10)
    print("Test 10:", days10, "->", res10)
    assert res10 == 21  # 1+2+3+4+5+6 = 21

    print("All tests passed!")


if __name__ == "__main__":
    test_totalMoney()