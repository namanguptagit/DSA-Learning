from functools import cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dp(index, current_set, can_change):
            if index == len(s):
                return 0
            character_index = ord(s[index]) - ord('a')
            
            current_set_updated = current_set | (1 << character_index)
            distinct_count = current_set_updated.bit_count()

            if distinct_count > k:
                res = 1 + dp(index + 1, 1 << character_index, can_change)
            else:
                res = dp(index + 1, current_set_updated, can_change)

            if can_change:
                for new_char_index in range(26):
                    new_set = current_set | (1 << new_char_index)
                    new_distinct_count = new_set.bit_count()

                    if new_distinct_count > k:
                        res = max(res, 1 + dp(index + 1, 1 << new_char_index, False))
                    else:
                        res = max(res, dp(index + 1, new_set, False))
            return res

        return dp(0, 0, True) + 1


# Simple tests consistent with repository style (print + assert)
def test_maxPartitionsAfterOperations():
    solver = Solution()

    # Test 1: Single character, k=1 -> 1
    s1, k1 = "a", 1
    res1 = solver.maxPartitionsAfterOperations(s1, k1)
    print("Test 1:", s1, k1, "->", res1)
    assert res1 == 1

    # Test 2: Two same chars, k=1; can change one to increase partitions -> 2
    s2, k2 = "aa", 1
    res2 = solver.maxPartitionsAfterOperations(s2, k2)
    print("Test 2:", s2, k2, "->", res2)
    assert res2 == 2

    # Test 3: Two different chars, k=1 -> 2 (cannot exceed length)
    s3, k3 = "ab", 1
    res3 = solver.maxPartitionsAfterOperations(s3, k3)
    print("Test 3:", s3, k3, "->", res3)
    assert res3 == 2

    # Test 4: Three different chars, k=1 -> 3
    s4, k4 = "abc", 1
    res4 = solver.maxPartitionsAfterOperations(s4, k4)
    print("Test 4:", s4, k4, "->", res4)
    assert res4 == 3

    print("All tests passed!")


if __name__ == "__main__":
    test_maxPartitionsAfterOperations()