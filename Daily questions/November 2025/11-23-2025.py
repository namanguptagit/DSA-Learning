class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum_ = 0

        min1 = min2 = float('inf')
        min11 = min22 = float('inf')

        for x in nums:
            sum_ += x
            r = x % 3

            if r == 1:
                if x < min1:
                    min11, min1 = min1, x
                elif x < min11:
                    min11 = x
            elif r == 2:
                if x < min2:
                    min22, min2 = min2, x
                elif x < min22:
                    min22 = x

        rem = sum_ % 3

        if rem == 0:
            return sum_

        if rem == 1:
            r1 = min1
            r2 = min2 + min22 if min2 < float('inf') and min22 < float('inf') else float('inf')
            remove = min(r1, r2)
            return 0 if remove == float('inf') else sum_ - remove
        else:
            r1 = min2
            r2 = min1 + min11 if min1 < float('inf') and min11 < float('inf') else float('inf')
            remove = min(r1, r2)
            result = 0 if remove == float('inf') else sum_ - remove
            return result
# Simple tests consistent with repository style (print + assert)
def test_maxSumDivThree():
    solver = Solution()

    # Test 1: Example from LeetCode
    nums1 = [3,6,5,1,8]
    expected1 = 18  # Remove 1 and 5 for sum 18
    out1 = solver.maxSumDivThree(nums1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: All numbers divisible by 3
    nums2 = [3, 9, 12]
    expected2 = 24
    out2 = solver.maxSumDivThree(nums2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: None divisible by 3, can't make sum divisible by 3 except 0
    nums3 = [1, 2, 4]
    expected3 = 6
    out3 = solver.maxSumDivThree(nums3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: All ones
    nums4 = [1, 1, 1, 1]
    expected4 = 3
    out4 = solver.maxSumDivThree(nums4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Single element divisible by 3
    nums5 = [9]
    expected5 = 9
    out5 = solver.maxSumDivThree(nums5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Single element not divisible by 3
    nums6 = [10]
    expected6 = 0
    out6 = solver.maxSumDivThree(nums6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Empty list
    nums7 = []
    expected7 = 0
    out7 = solver.maxSumDivThree(nums7)
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: Negative numbers (should work similarly)
    nums8 = [3, 6, -1, 4]
    expected8 = 12  # Remove -1 to maximize: 3 + 6 + 4 = 13, but 13 % 3 == 1; remove -1: sum=14; 14%3==2; try removing two 1-rem numbers; just 14-4=10, so better to use 12, sum without -1 and 4.
    out8 = solver.maxSumDivThree(nums8)
    print("Test 8:", out8)
    # Let's check: sum=12 (3+6+4-1=12); 12%3==0, so 12 is possible.
    assert out8 == 12

    # Test 9: Large numbers
    nums9 = [333, 2, 2, 2, 2, 999]
    expected9 = 1336  # sum=1340, 1340%3=1; smallest way to remove 2 or 2+2=4; so remove one 2: 1338, 1338%3=0, next best is 1336 (removing three 2s? 1334, but 1334%3=1)
    out9 = solver.maxSumDivThree(nums9)
    print("Test 9:", out9)
    assert out9 == 1338

    # Test 10: All twos
    nums10 = [2,2,2]
    expected10 = 6
    out10 = solver.maxSumDivThree(nums10)
    print("Test 10:", out10)
    assert out10 == expected10

    print("All tests passed for maxSumDivThree.")

if __name__ == "__main__":
    # Needed since the function uses List[int], import typing.List if not imported in this file
    # from typing import List
    test_maxSumDivThree()