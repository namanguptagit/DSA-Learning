class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        count = 0

        while i < j:
            total = nums[i] + nums[j]
            if total == k:
                count += 1
                i += 1
                j -= 1
            elif total > k:
                j -= 1
            else:
                i += 1

        return count

# Simple tests consistent with repository style (print + assert)
def test_maxOperations():
    solver = Solution()

    # Test 1: Example from Leetcode
    nums1 = [1,2,3,4]
    k1 = 5
    expected1 = 2
    out1 = solver.maxOperations(nums1[:], k1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: All pairs possible
    nums2 = [3,1,3,4,3]
    k2 = 6
    expected2 = 1
    out2 = solver.maxOperations(nums2[:], k2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: All same number, pair sum not possible
    nums3 = [2,2,2,2]
    k3 = 5
    expected3 = 0
    out3 = solver.maxOperations(nums3[:], k3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Large array, many pairs
    nums4 = [1,5,1,5,1,5,1,5]
    k4 = 6
    expected4 = 4
    out4 = solver.maxOperations(nums4[:], k4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: No valid pairs
    nums5 = [1,2,3,4]
    k5 = 8
    expected5 = 0
    out5 = solver.maxOperations(nums5[:], k5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Only one pair
    nums6 = [1,2,3,4,5]
    k6 = 9
    expected6 = 1
    out6 = solver.maxOperations(nums6[:], k6)
    print("Test 6:", out6)
    assert out6 == expected6

    print("All tests passed for maxOperations.")

if __name__ == "__main__":
    test_maxOperations()