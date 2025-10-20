class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        # this map holds the new value of every digit after addition by a % 10
        incremented = {str(n):str((n+a)%10) for n in range(10)}

        # function applying the addition operation
        def addOp(s):
            res = ""
            for i in range(n):
                res += s[i] if i % 2 == 0 else incremented[s[i]]
            return res

        # function applying the rotation operation
        def rotOp(s):
            return s[n-b:] + s[:n-b]


        seen = set()
        def dfs(s):
            if s in seen:
                return
            seen.add(s)
            dfs(addOp(s))
            dfs(rotOp(s))
            return

        dfs(s)
        return min(seen)


# Simple tests consistent with repository style (print + assert)
def test_findLexSmallestString():
    solver = Solution()

    # Test 1: Simple case with no operations needed
    s1, a1, b1 = "1234", 0, 0
    res1 = solver.findLexSmallestString(s1, a1, b1)
    print("Test 1:", s1, a1, b1, "->", res1)
    assert res1 == "1234"

    # Test 2: Addition operation only
    s2, a2, b2 = "1234", 1, 0
    res2 = solver.findLexSmallestString(s2, a2, b2)
    print("Test 2:", s2, a2, b2, "->", res2)
    assert res2 == "1334"

    # Test 3: Rotation operation only
    s3, a3, b3 = "1234", 0, 1
    res3 = solver.findLexSmallestString(s3, a3, b3)
    print("Test 3:", s3, a3, b3, "->", res3)
    assert res3 == "4123"

    # Test 4: Both operations
    s4, a4, b4 = "1234", 1, 1
    res4 = solver.findLexSmallestString(s4, a4, b4)
    print("Test 4:", s4, a4, b4, "->", res4)
    assert res4 == "1234"

    # Test 5: Larger addition value
    s5, a5, b5 = "1234", 5, 0
    res5 = solver.findLexSmallestString(s5, a5, b5)
    print("Test 5:", s5, a5, b5, "->", res5)
    assert res5 == "1734"

    # Test 6: Larger rotation value
    s6, a6, b6 = "1234", 0, 2
    res6 = solver.findLexSmallestString(s6, a6, b6)
    print("Test 6:", s6, a6, b6, "->", res6)
    assert res6 == "3412"

    # Test 7: Single character string
    s7, a7, b7 = "5", 1, 0
    res7 = solver.findLexSmallestString(s7, a7, b7)
    print("Test 7:", s7, a7, b7, "->", res7)
    assert res7 == "5"

    # Test 8: Two character string
    s8, a8, b8 = "12", 1, 1
    res8 = solver.findLexSmallestString(s8, a8, b8)
    print("Test 8:", s8, a8, b8, "->", res8)
    assert res8 == "12"

    print("All tests passed!")


if __name__ == "__main__":
    test_findLexSmallestString()