class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        bits.pop()
        n = len(bits)

        if n == 0 or bits[-1] == 0:
            return True

        ones = 0
        for i in range(n - 1, -1, -1):
            if bits[i] == 1:
                ones += 1
            else:
                break

        return not (ones & 1)

# Simple tests consistent with repository style (print + assert)
def test_isOneBitCharacter():
    solver = Solution()

    # Test 1: Ends with single 0
    bits1 = [1, 0, 0]
    expected1 = True
    out1 = solver.isOneBitCharacter(bits1[:])
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Last character is part of two-bit char
    bits2 = [1, 1, 1, 0]
    expected2 = False
    out2 = solver.isOneBitCharacter(bits2[:])
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Single 0
    bits3 = [0]
    expected3 = True
    out3 = solver.isOneBitCharacter(bits3[:])
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Only two-bit char
    bits4 = [1, 0]
    expected4 = False
    out4 = solver.isOneBitCharacter(bits4[:])
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: All single bits
    bits5 = [0,0,0,0]
    expected5 = True
    out5 = solver.isOneBitCharacter(bits5[:])
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Long sequence, ends with 0
    bits6 = [1,1,0,0]
    expected6 = True
    out6 = solver.isOneBitCharacter(bits6[:])
    print("Test 6:", out6)
    assert out6 == expected6

    print("All tests passed for isOneBitCharacter.")

if __name__ == "__main__":
    test_isOneBitCharacter()