class Solution:
    def pairSum(self, head):
        slow = head
        fast = head
        maxVal = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        nextNode, prev = None, None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxVal

# ---- Simple tests consistent with repository style (print + assert) ----
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked(lst):
    """Helper to convert list to linked list."""
    if not lst:
        return None
    dummy = ListNode(0)
    curr = dummy
    for v in lst:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def test_pairSum():
    solver = Solution()

    # Test 1: Example from problem [5,4,2,1] → 6
    l1 = list_to_linked([5,4,2,1])
    out1 = solver.pairSum(l1)
    print("Test 1:", out1)
    assert out1 == 6

    # Test 2: Even-length, all identical [7,7,7,7] → 14
    l2 = list_to_linked([7,7,7,7])
    out2 = solver.pairSum(l2)
    print("Test 2:", out2)
    assert out2 == 14

    # Test 3: Even-length, increasing [1,2,3,4] → 5
    l3 = list_to_linked([1,2,3,4])
    out3 = solver.pairSum(l3)
    print("Test 3:", out3)
    assert out3 == 5

    # Test 4: Even-length, decreasing [4,3,2,1] → 5
    l4 = list_to_linked([4,3,2,1])
    out4 = solver.pairSum(l4)
    print("Test 4:", out4)
    assert out4 == 5

    # Test 5: Two-node list [1,100] → 101
    l5 = list_to_linked([1,100])
    out5 = solver.pairSum(l5)
    print("Test 5:", out5)
    assert out5 == 101

    # Test 6: Four nodes with tie [1,2,2,1] → 3
    l6 = list_to_linked([1,2,2,1])
    out6 = solver.pairSum(l6)
    print("Test 6:", out6)
    assert out6 == 3

    # Test 7: Large values [1000,2000,3000,4000] → 5000
    l7 = list_to_linked([1000,2000,3000,4000])
    out7 = solver.pairSum(l7)
    print("Test 7:", out7)
    assert out7 == 5000

if __name__ == "__main__":
    test_pairSum()