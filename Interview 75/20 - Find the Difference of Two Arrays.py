# brute force approach
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        r1,r2 = [],[]
        l = max(len(nums1),len(nums2))
        for i in range(0,l):
            if i<len(nums1):
                if nums1[i] not in nums2:
                    if nums1[i] not in r1:
                        r1.append(nums1[i])
            if i<len(nums2):
                if nums2[i] not in nums1:
                    if nums2[i] not in r2:
                        r2.append(nums2[i])
        return [r1,r2]
# Optimised approach using sets
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

# Simple tests consistent with repository style (print + assert)
def test_findDifference():
    solver = Solution()

    # Test 1: Typical example
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    expected1 = [[1,3],[4,6]]
    out1 = solver.findDifference(nums1, nums2)
    print("Test 1:", out1)
    assert sorted(out1[0]) == sorted(expected1[0]) and sorted(out1[1]) == sorted(expected1[1])

    # Test 2: All same elements
    nums1 = [1,1,1]
    nums2 = [1,1]
    expected2 = [[],[]]
    out2 = solver.findDifference(nums1, nums2)
    print("Test 2:", out2)
    assert sorted(out2[0]) == sorted(expected2[0]) and sorted(out2[1]) == sorted(expected2[1])

    # Test 3: nums1 is empty
    nums1 = []
    nums2 = [1,2,3]
    expected3 = [[], [1,2,3]]
    out3 = solver.findDifference(nums1, nums2)
    print("Test 3:", out3)
    assert sorted(out3[0]) == sorted(expected3[0]) and sorted(out3[1]) == sorted(expected3[1])

    # Test 4: nums2 is empty
    nums1 = [2,5,7]
    nums2 = []
    expected4 = [[2,5,7], []]
    out4 = solver.findDifference(nums1, nums2)
    print("Test 4:", out4)
    assert sorted(out4[0]) == sorted(expected4[0]) and sorted(out4[1]) == sorted(expected4[1])

    # Test 5: Both empty
    nums1 = []
    nums2 = []
    expected5 = [[],[]]
    out5 = solver.findDifference(nums1, nums2)
    print("Test 5:", out5)
    assert sorted(out5[0]) == sorted(expected5[0]) and sorted(out5[1]) == sorted(expected5[1])

    # Test 6: Negative numbers and overlap
    nums1 = [1,-2,3]
    nums2 = [3,-2,9]
    expected6 = [[1], [9]]
    out6 = solver.findDifference(nums1, nums2)
    print("Test 6:", out6)
    assert sorted(out6[0]) == sorted(expected6[0]) and sorted(out6[1]) == sorted(expected6[1])

if __name__ == "__main__":
    test_findDifference()