from itertools import permutations

class Solution:
    balanced_numbers = None

    @staticmethod
    def init_balanced_numbers():
        s = set()
        bases = [
            "1", "22", "122", "333", "1333", "4444", "14444", "22333", "55555",
            "122333", "155555", "224444", "666666", "1224444", "1666666",
            "2255555", "3334444", "7777777", "12255555"
        ]

        for base in bases:
            for p in set(permutations(sorted(base))):
                s.add(int("".join(p)))
        return sorted(s)

    def __init__(self):
        if Solution.balanced_numbers is None:
            Solution.balanced_numbers = Solution.init_balanced_numbers()

    def nextBeautifulNumber(self, n: int) -> int:
        for x in Solution.balanced_numbers:
            if x > n:
                return x
        return -1


# Simple tests consistent with repository style (print + assert)
def test_nextBeautifulNumber():
    solver = Solution()

    # Test 1: Small number
    n1 = 1
    res1 = solver.nextBeautifulNumber(n1)
    print("Test 1:", n1, "->", res1)
    assert res1 == 22

    # Test 2: Number that equals a balanced number
    n2 = 22
    res2 = solver.nextBeautifulNumber(n2)
    print("Test 2:", n2, "->", res2)
    assert res2 == 122

    # Test 3: Number between balanced numbers
    n3 = 100
    res3 = solver.nextBeautifulNumber(n3)
    print("Test 3:", n3, "->", res3)
    assert res3 == 122

    # Test 4: Larger number
    n4 = 1000
    res4 = solver.nextBeautifulNumber(n4)
    print("Test 4:", n4, "->", res4)
    assert res4 == 1333

    # Test 5: Number close to a balanced number
    n5 = 122
    res5 = solver.nextBeautifulNumber(n5)
    print("Test 5:", n5, "->", res5)
    assert res5 == 333

    # Test 6: Very small number
    n6 = 0
    res6 = solver.nextBeautifulNumber(n6)
    print("Test 6:", n6, "->", res6)
    assert res6 == 1

    # Test 7: Number that's a balanced number itself
    n7 = 333
    res7 = solver.nextBeautifulNumber(n7)
    print("Test 7:", n7, "->", res7)
    assert res7 == 4444

    # Test 8: Large number
    n8 = 10000
    res8 = solver.nextBeautifulNumber(n8)
    print("Test 8:", n8, "->", res8)
    assert res8 == 13333

    # Test 9: Number between larger balanced numbers
    n9 = 5000
    res9 = solver.nextBeautifulNumber(n9)
    print("Test 9:", n9, "->", res9)
    assert res9 == 55555

    # Test 10: Edge case with negative number
    n10 = -1
    res10 = solver.nextBeautifulNumber(n10)
    print("Test 10:", n10, "->", res10)
    assert res10 == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_nextBeautifulNumber()