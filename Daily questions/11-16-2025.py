class Solution:
    def numSub(self, s: str) -> int:
        mod=10**9+7
        count=0
        ans=0
        for c in s:
            is0=c=='0'
            ans+=(-is0 & count*(count+1)//2)
            ans%=mod
            count=(-(not is0) & count+1)
        ans=ans+count*(count+1)//2%mod
        return ans

# Simple tests consistent with repository style (print + assert)
def test_numSub():
    solver = Solution()

    # Test 1: Simple example
    s1 = "0110111"
    expected1 = 9   # substrings: 1,1,1,11,11,111,1,1
    out1 = solver.numSub(s1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: All zeros
    s2 = "0000"
    expected2 = 0
    out2 = solver.numSub(s2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: All ones
    s3 = "1111"
    expected3 = 10  # 1+2+3+4 = 10
    out3 = solver.numSub(s3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Single zero
    s4 = "0"
    expected4 = 0
    out4 = solver.numSub(s4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Single one
    s5 = "1"
    expected5 = 1
    out5 = solver.numSub(s5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Alternating 10101
    s6 = "10101"
    expected6 = 3
    out6 = solver.numSub(s6)
    print("Test 6:", out6)
    assert out6 == expected6

    print("All tests passed for numSub.")

if __name__ == "__main__":
    test_numSub()