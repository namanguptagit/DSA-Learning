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
# Helper class for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

# Helper function to convert linked list to list
def linked_list_to_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

# Simple tests consistent with repository style (print + assert)
def test_oddEvenList():
    solver = Solution()

    # Test 1: Odd and even length list
    list1 = create_linked_list([1,2,3,4,5])
    expected1 = [1,3,5,2,4]
    out1 = linked_list_to_list(solver.oddEvenList(list1))
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Even length list
    list2 = create_linked_list([2,1,3,5,6,4,7])
    expected2 = [2,3,6,7,1,5,4]
    out2 = linked_list_to_list(solver.oddEvenList(list2))
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: Single element
    list3 = create_linked_list([42])
    expected3 = [42]
    out3 = linked_list_to_list(solver.oddEvenList(list3))
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: Two elements
    list4 = create_linked_list([1,2])
    expected4 = [1,2]
    out4 = linked_list_to_list(solver.oddEvenList(list4))
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Three elements
    list5 = create_linked_list([1,2,3])
    expected5 = [1,3,2]
    out5 = linked_list_to_list(solver.oddEvenList(list5))
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Empty list
    list6 = create_linked_list([])
    expected6 = []
    out6 = linked_list_to_list(solver.oddEvenList(list6))
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: Four elements
    list7 = create_linked_list([10,20,30,40])
    expected7 = [10,30,20,40]
    out7 = linked_list_to_list(solver.oddEvenList(list7))
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for oddEvenList.")

if __name__ == "__main__":
    test_oddEvenList()
