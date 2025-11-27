# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  
        curr = head 

        while curr:
            temp = curr.next  
            curr.next = prev 
            prev = curr       
            curr = temp      

        return prev

# ---- Simple tests consistent with repository style (print + assert) ----
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

def test_reverseList():
    solver = Solution()
    
    # Test 1: Standard case
    l1 = list_to_linked([1,2,3,4,5])
    out1 = solver.reverseList(l1)
    print("Test 1:", linked_to_list(out1))
    assert linked_to_list(out1) == [5,4,3,2,1]

    # Test 2: Single element list
    l2 = list_to_linked([1])
    out2 = solver.reverseList(l2)
    print("Test 2:", linked_to_list(out2))
    assert linked_to_list(out2) == [1]

    # Test 3: Empty list
    l3 = list_to_linked([])
    out3 = solver.reverseList(l3)
    print("Test 3:", linked_to_list(out3))
    assert linked_to_list(out3) == []

    # Test 4: Two element list
    l4 = list_to_linked([7,9])
    out4 = solver.reverseList(l4)
    print("Test 4:", linked_to_list(out4))
    assert linked_to_list(out4) == [9,7]

    # Test 5: All identical values
    l5 = list_to_linked([4,4,4,4])
    out5 = solver.reverseList(l5)
    print("Test 5:", linked_to_list(out5))
    assert linked_to_list(out5) == [4,4,4,4]

if __name__ == "__main__":
    test_reverseList()