class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head              # head of odd list
        even = head.next        # head of even list
        even_head = even        # to connect later
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        odd.next = even_head    # join odd list with even list
        return head
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

def test_oddEvenList():
    solver = Solution()
    
    # Test 1: Example from problem, [1,2,3,4,5] => [1,3,5,2,4]
    l1 = list_to_linked([1,2,3,4,5])
    out1 = solver.oddEvenList(l1)
    print("Test 1:", linked_to_list(out1))
    assert linked_to_list(out1) == [1,3,5,2,4]

    # Test 2: Even number of nodes [2,1,3,5,6,4,7] => [2,3,6,7,1,5,4]
    l2 = list_to_linked([2,1,3,5,6,4,7])
    out2 = solver.oddEvenList(l2)
    print("Test 2:", linked_to_list(out2))
    assert linked_to_list(out2) == [2,3,6,7,1,5,4]

    # Test 3: List of length 1
    l3 = list_to_linked([8])
    out3 = solver.oddEvenList(l3)
    print("Test 3:", linked_to_list(out3))
    assert linked_to_list(out3) == [8]

    # Test 4: List of length 2
    l4 = list_to_linked([10,11])
    out4 = solver.oddEvenList(l4)
    print("Test 4:", linked_to_list(out4))
    assert linked_to_list(out4) == [10,11]

    # Test 5: Empty list
    l5 = list_to_linked([])
    out5 = solver.oddEvenList(l5)
    print("Test 5:", linked_to_list(out5))
    assert linked_to_list(out5) == []

    # Test 6: Three node list [1,2,3]
    l6 = list_to_linked([1,2,3])
    out6 = solver.oddEvenList(l6)
    print("Test 6:", linked_to_list(out6))
    assert linked_to_list(out6) == [1,3,2]

    # Test 7: All odds [1,3,5,7]
    l7 = list_to_linked([1,3,5,7])
    out7 = solver.oddEvenList(l7)
    print("Test 7:", linked_to_list(out7))
    assert linked_to_list(out7) == [1,5,3,7]

    # Test 8: All evens [2,4,6,8]
    l8 = list_to_linked([2,4,6,8])
    out8 = solver.oddEvenList(l8)
    print("Test 8:", linked_to_list(out8))
    assert linked_to_list(out8) == [2,6,4,8]

if __name__ == "__main__":
    test_oddEvenList()
