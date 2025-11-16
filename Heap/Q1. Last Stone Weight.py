import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert to max-heap by negating values
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)  # heaviest
            second = -heapq.heappop(max_heap) # second heaviest
            
            if first != second:
                heapq.heappush(max_heap, -(first - second))
        
        return -max_heap[0] if max_heap else 0

# Simple tests consistent with repository style (print + assert)
def test_lastStoneWeight():
    solver = Solution()

    # Test 1: Basic example
    stones1 = [2,7,4,1,8,1]
    expected1 = 1
    out1 = solver.lastStoneWeight(stones1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: All same stones
    stones2 = [5,5,5,5]
    expected2 = 0
    out2 = solver.lastStoneWeight(stones2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Only one stone
    stones3 = [6]
    expected3 = 6
    out3 = solver.lastStoneWeight(stones3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Two stones, different
    stones4 = [10,4]
    expected4 = 6
    out4 = solver.lastStoneWeight(stones4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: No stones
    stones5 = []
    expected5 = 0
    out5 = solver.lastStoneWeight(stones5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: All ones
    stones6 = [1,1,1,1,1]
    expected6 = 1
    out6 = solver.lastStoneWeight(stones6)
    print("Test 6:", out6)
    assert out6 == expected6

    print("All tests passed for lastStoneWeight.")

if __name__ == "__main__":
    test_lastStoneWeight()