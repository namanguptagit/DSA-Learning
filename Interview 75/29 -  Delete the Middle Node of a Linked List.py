# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head     

# Simple tests consistent with repository style (print + assert)
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

def linked_to_list(head):
    """Helper to convert linked list to list."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def test_deleteMiddle():
    solver = Solution()
    
    # Test 1: Example given in problem: [1,3,4,7,1,2,6]
    l1 = list_to_linked([1,3,4,7,1,2,6])
    out1 = solver.deleteMiddle(l1)
    print("Test 1:", linked_to_list(out1))
    assert linked_to_list(out1) == [1,3,4,1,2,6]  # Middle value 7 removed

    # Test 2: Length 1 (should return None)
    l2 = list_to_linked([1])
    out2 = solver.deleteMiddle(l2)
    print("Test 2:", out2)
    assert out2 is None

    # Test 3: Length 2 (removes second/last node)
    l3 = list_to_linked([1,2])
    out3 = solver.deleteMiddle(l3)
    print("Test 3:", linked_to_list(out3))
    assert linked_to_list(out3) == [1]

    # Test 4: Odd length
    l4 = list_to_linked([10,20,30])
    out4 = solver.deleteMiddle(l4)
    print("Test 4:", linked_to_list(out4))
    assert linked_to_list(out4) == [10,30]

    # Test 5: Even length
    l5 = list_to_linked([11,22,33,44])
    out5 = solver.deleteMiddle(l5)
    print("Test 5:", linked_to_list(out5))
    assert linked_to_list(out5) == [11,22,44]

    # Test 6: All identical elements
    l6 = list_to_linked([5,5,5,5,5])
    out6 = solver.deleteMiddle(l6)
    print("Test 6:", linked_to_list(out6))
    assert linked_to_list(out6) == [5,5,5,5]

if __name__ == "__main__":
    test_deleteMiddle()