class RecentCounter:
    def __init__(self):
        self.records = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.start] < t - 3000:
            self.start += 1
        return len(self.records) - self.start

# Simple tests consistent with repository style (print + assert)
def test_RecentCounter():
    # Test 1: Example from problem
    rc = RecentCounter()
    out1 = rc.ping(1)
    print("Test 1.1:", out1)
    assert out1 == 1

    out2 = rc.ping(100)
    print("Test 1.2:", out2)
    assert out2 == 2

    out3 = rc.ping(3001)
    print("Test 1.3:", out3)
    assert out3 == 3

    out4 = rc.ping(3002)
    print("Test 1.4:", out4)
    assert out4 == 3

    # Test 2: Large gap between pings
    rc2 = RecentCounter()
    out5 = rc2.ping(1)
    out6 = rc2.ping(4000)
    out7 = rc2.ping(8000)
    print("Test 2.1:", out5)
    print("Test 2.2:", out6)
    print("Test 2.3:", out7)
    assert out5 == 1
    assert out6 == 1
    assert out7 == 1

    # Test 3: Consecutive calls at the same time
    rc3 = RecentCounter()
    out8 = rc3.ping(10)
    out9 = rc3.ping(10)
    out10 = rc3.ping(10)
    print("Test 3.1:", out8)
    print("Test 3.2:", out9)
    print("Test 3.3:", out10)
    assert out8 == 1
    assert out9 == 2
    assert out10 == 3

    # Test 4: All pings within 3000 ms window
    rc4 = RecentCounter()
    times = [50, 1000, 2000, 2500, 2999]
    results = [rc4.ping(x) for x in times]
    print("Test 4:", results)
    assert results == [1,2,3,4,5]

    print("All tests passed for RecentCounter.")

if __name__ == "__main__":
    test_RecentCounter()