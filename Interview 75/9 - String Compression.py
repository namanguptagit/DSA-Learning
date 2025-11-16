class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        idx = 0
        i = 0
        while i < n:
            ch = chars[i]
            count = 0
            while i < n and chars[i] == ch:
                count += 1
                i += 1
            if count == 1:
                chars[idx] = ch
                idx += 1
            else:
                chars[idx] = ch
                idx += 1
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1
        chars[:] = chars[:idx]
        return idx

# Simple tests consistent with repository style (print + assert)
def test_compress():
    solver = Solution()

    # Test 1: Basic example
    chars1 = ["a","a","b","b","c","c","c"]
    expected1 = ["a","2","b","2","c","3"]
    out1 = solver.compress(chars1)
    print("Test 1:", chars1[:out1])
    assert out1 == 6
    assert chars1[:out1] == expected1

    # Test 2: No compression needed (all singles)
    chars2 = ["a","b","c"]
    expected2 = ["a","b","c"]
    out2 = solver.compress(chars2)
    print("Test 2:", chars2[:out2])
    assert out2 == 3
    assert chars2[:out2] == expected2

    # Test 3: All characters same
    chars3 = ["a","a","a","a"]
    expected3 = ["a","4"]
    out3 = solver.compress(chars3)
    print("Test 3:", chars3[:out3])
    assert out3 == 2
    assert chars3[:out3] == expected3

    # Test 4: Single element
    chars4 = ["z"]
    expected4 = ["z"]
    out4 = solver.compress(chars4)
    print("Test 4:", chars4[:out4])
    assert out4 == 1
    assert chars4[:out4] == expected4

    # Test 5: Mixed single and multiple groups
    chars5 = ["a","b","b","c","c","c","d"]
    expected5 = ["a","b","2","c","3","d"]
    out5 = solver.compress(chars5)
    print("Test 5:", chars5[:out5])
    assert out5 == 6
    assert chars5[:out5] == expected5

    # Test 6: Numbers >9
    chars6 = ["a"]*12
    expected6 = ["a","1","2"]
    out6 = solver.compress(chars6)
    print("Test 6:", chars6[:out6])
    assert out6 == 3
    assert chars6[:out6] == expected6

    print("All tests passed for compress.")

if __name__ == "__main__":
    test_compress()