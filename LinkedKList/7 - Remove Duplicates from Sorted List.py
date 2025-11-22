class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next   # Skip duplicate
            else:
                current = current.next  # Move forward
        
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
def test_deleteDuplicates():
    solver = Solution()

    # Test 1: Duplicates at start and end
    list1 = create_linked_list([1,1,2,3,3])
    expected1 = [1,2,3]
    out1 = linked_list_to_list(solver.deleteDuplicates(list1))
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Multiple consecutive duplicates
    list2 = create_linked_list([1,1,1,2,3,3,4])
    expected2 = [1,2,3,4]
    out2 = linked_list_to_list(solver.deleteDuplicates(list2))
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: No duplicates
    list3 = create_linked_list([1,2,3,4,5])
    expected3 = [1,2,3,4,5]
    out3 = linked_list_to_list(solver.deleteDuplicates(list3))
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: All elements the same
    list4 = create_linked_list([2,2,2,2])
    expected4 = [2]
    out4 = linked_list_to_list(solver.deleteDuplicates(list4))
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Empty list
    list5 = create_linked_list([])
    expected5 = []
    out5 = linked_list_to_list(solver.deleteDuplicates(list5))
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: Only one element
    list6 = create_linked_list([42])
    expected6 = [42]
    out6 = linked_list_to_list(solver.deleteDuplicates(list6))
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: List with two different numbers
    list7 = create_linked_list([4,5])
    expected7 = [4,5]
    out7 = linked_list_to_list(solver.deleteDuplicates(list7))
    print("Test 7:", out7)
    assert out7 == expected7

    print("All tests passed for deleteDuplicates.")

if __name__ == "__main__":
    test_deleteDuplicates()