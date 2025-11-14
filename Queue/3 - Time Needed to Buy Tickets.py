class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        time = 0

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], target)
            else:
                time += min(tickets[i], target - 1)
        return time

# Simple tests consistent with repository style (print + assert)
def test_timeRequiredToBuy():
    solver = Solution()

    # Test 1: Example from LeetCode
    tickets1 = [2,3,2]
    k1 = 2
    res1 = solver.timeRequiredToBuy(tickets1.copy(), k1)
    print("Test 1:", res1)
    assert res1 == 6

    # Test 2: Single person
    tickets2 = [5]
    k2 = 0
    res2 = solver.timeRequiredToBuy(tickets2.copy(), k2)
    print("Test 2:", res2)
    assert res2 == 5

    # Test 3: All ones
    tickets3 = [1,1,1,1]
    k3 = 2
    res3 = solver.timeRequiredToBuy(tickets3.copy(), k3)
    print("Test 3:", res3)
    assert res3 == 3

    # Test 4: Person k has the most tickets
    tickets4 = [2,2,10,2,2]
    k4 = 2
    res4 = solver.timeRequiredToBuy(tickets4.copy(), k4)
    print("Test 4:", res4)
    assert res4 == 14

    # Test 5: k is first
    tickets5 = [4,2,1]
    k5 = 0
    res5 = solver.timeRequiredToBuy(tickets5.copy(), k5)
    print("Test 5:", res5)
    assert res5 == 4

    # Test 6: k is last
    tickets6 = [1,2,4]
    k6 = 2
    res6 = solver.timeRequiredToBuy(tickets6.copy(), k6)
    print("Test 6:", res6)
    assert res6 == 6

    # Test 7: All zeros (not typical input, but check anyway)
    tickets7 = [0,0,0,0]
    k7 = 2
    res7 = solver.timeRequiredToBuy(tickets7.copy(), k7)
    print("Test 7:", res7)
    assert res7 == 0

    print("All tests passed for timeRequiredToBuy.")

if __name__ == "__main__":
    test_timeRequiredToBuy()