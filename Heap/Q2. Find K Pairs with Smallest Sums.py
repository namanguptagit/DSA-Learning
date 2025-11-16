import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        min_heap = []
        result = []
        
        # initialize heap with pairs (nums1[i], nums2[0])
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        # extract k smallest pairs
        while min_heap and len(result) < k:
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # push next pair with nums2[j+1]
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
        
        return result

# Simple tests consistent with repository style (print + assert)
def test_kSmallestPairs():
    solver = Solution()

    # Test 1: Basic example
    nums1_1 = [1,7,11]
    nums2_1 = [2,4,6]
    k1 = 3
    expected1 = [[1,2],[1,4],[1,6]]
    out1 = solver.kSmallestPairs(nums1_1, nums2_1, k1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Both arrays have length 1
    nums1_2 = [1]
    nums2_2 = [2]
    k2 = 1
    expected2 = [[1,2]]
    out2 = solver.kSmallestPairs(nums1_2, nums2_2, k2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: k larger than all possible pairs
    nums1_3 = [1,2]
    nums2_3 = [3]
    k3 = 10
    expected3 = [[1,3], [2,3]]
    out3 = solver.kSmallestPairs(nums1_3, nums2_3, k3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: One array empty
    nums1_4 = []
    nums2_4 = [1,2,3]
    k4 = 2
    expected4 = []
    out4 = solver.kSmallestPairs(nums1_4, nums2_4, k4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Both arrays empty
    nums1_5 = []
    nums2_5 = []
    k5 = 5
    expected5 = []
    out5 = solver.kSmallestPairs(nums1_5, nums2_5, k5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: k is zero
    nums1_6 = [1,2]
    nums2_6 = [3,4]
    k6 = 0
    expected6 = []
    out6 = solver.kSmallestPairs(nums1_6, nums2_6, k6)
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Duplicates present
    nums1_7 = [1,1,2]
    nums2_7 = [1,2,3]
    k7 = 4
    expected7 = [[1,1],[1,1],[1,2],[1,2]]
    out7 = solver.kSmallestPairs(nums1_7, nums2_7, k7)
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for kSmallestPairs.")

if __name__ == "__main__":
    test_kSmallestPairs()