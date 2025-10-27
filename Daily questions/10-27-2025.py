from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams, prev = 0, 0
        for row in bank:
            devices = row.count("1")
            if devices:
                beams += prev * devices
                prev = devices
        return beams


# Simple tests consistent with repository style (print + assert)
def test_numberOfBeams():
    solver = Solution()

    # Test 1: Single row with devices
    bank1 = ["011001"]
    res1 = solver.numberOfBeams(bank1)
    print("Test 1:", bank1, "->", res1)
    assert res1 == 0

    # Test 2: Two rows with devices
    bank2 = ["011001", "000000"]
    res2 = solver.numberOfBeams(bank2)
    print("Test 2:", bank2, "->", res2)
    assert res2 == 0

    # Test 3: Two rows with devices
    bank3 = ["011001", "000000", "010100"]
    res3 = solver.numberOfBeams(bank3)
    print("Test 3:", bank3, "->", res3)
    assert res3 == 4

    # Test 4: Multiple rows with devices
    bank4 = ["011001", "000000", "010100", "001000"]
    res4 = solver.numberOfBeams(bank4)
    print("Test 4:", bank4, "->", res4)
    assert res4 == 8

    # Test 5: No devices
    bank5 = ["000000", "000000", "000000"]
    res5 = solver.numberOfBeams(bank5)
    print("Test 5:", bank5, "->", res5)
    assert res5 == 0

    # Test 6: All devices in one row
    bank6 = ["111111"]
    res6 = solver.numberOfBeams(bank6)
    print("Test 6:", bank6, "->", res6)
    assert res6 == 0

    # Test 7: Pattern with gaps
    bank7 = ["010101", "000000", "000000", "101010"]
    res7 = solver.numberOfBeams(bank7)
    print("Test 7:", bank7, "->", res7)
    assert res7 == 18

    # Test 8: Empty bank
    bank8 = []
    res8 = solver.numberOfBeams(bank8)
    print("Test 8:", bank8, "->", res8)
    assert res8 == 0

    # Test 9: Specific example
    bank9 = ["000", "111", "000"]
    res9 = solver.numberOfBeams(bank9)
    print("Test 9:", bank9, "->", res9)
    assert res9 == 0

    # Test 10: Complex pattern
    bank10 = ["0000", "1111", "0000", "1111", "0000"]
    res10 = solver.numberOfBeams(bank10)
    print("Test 10:", bank10, "->", res10)
    assert res10 == 16

    print("All tests passed!")


if __name__ == "__main__":
    test_numberOfBeams()