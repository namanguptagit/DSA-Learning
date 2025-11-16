import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        total = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        while True:
            largest = -heapq.heappop(max_heap)
            rest = total - largest

            if largest == 1 or rest == 1:
                return True

            if rest == 0 or largest < rest:
                return False

            new_value = largest % rest
            if new_value == 0:
                return False

            total = rest + new_value
            heapq.heappush(max_heap, -new_value)

# Simple tests consistent with repository style (print + assert)
def test_isPossible():
    solver = Solution()

    # Test 1: Basic example
    target1 = [9,3,5]
    expected1 = True
    out1 = solver.isPossible(target1)
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Impossible to construct
    target2 = [1,1,1,2]
    expected2 = False
    out2 = solver.isPossible(target2)
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Simple possible case
    target3 = [8,5]
    expected3 = True
    out3 = solver.isPossible(target3)
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Only one element, which is 1
    target4 = [1]
    expected4 = True
    out4 = solver.isPossible(target4)
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Only one element, not 1
    target5 = [5]
    expected5 = False
    out5 = solver.isPossible(target5)
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Contains zeros (invalid case)
    target6 = [0,2]
    expected6 = False
    try:
        out6 = solver.isPossible(target6)
    except Exception:
        out6 = False  # Assume error means impossible
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: All ones
    target7 = [1,1,1]
    expected7 = True
    out7 = solver.isPossible(target7)
    print("Test 7:", out7)
    assert out7 == expected7

if __name__ == "__main__":
    test_isPossible()