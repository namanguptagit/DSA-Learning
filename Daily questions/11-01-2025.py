# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        # Step 1: Convert nums to a set for O(1) lookup
        num_set = set(nums)

        # Step 2: Create a dummy node pointing to head
        dummy = ListNode(0)
        dummy.next = head

        # Step 3: Use a pointer curr to traverse the list
        curr = dummy

        # Step 4: Traverse and remove nodes whose values are in num_set
        while curr.next:
            if curr.next.val in num_set:
                # Delete the node by skipping it
                curr.next = curr.next.next
            else:
                # Move to the next node
                curr = curr.next

        # Step 5: Return the modified list (skipping dummy node)
        return dummy.next


# Helper functions for testing
def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Simple tests consistent with repository style (print + assert)
def test_modifiedList():
    solver = Solution()

    # Test 1: Remove single value from middle
    nums1, head1 = [2], create_linked_list([1, 2, 3])
    res1 = solver.modifiedList(nums1, head1)
    result1 = linked_list_to_list(res1)
    print("Test 1:", nums1, "[1,2,3]", "->", result1)
    assert result1 == [1, 3]

    # Test 2: Remove multiple values
    nums2, head2 = [1, 3], create_linked_list([1, 2, 3, 4])
    res2 = solver.modifiedList(nums2, head2)
    result2 = linked_list_to_list(res2)
    print("Test 2:", nums2, "[1,2,3,4]", "->", result2)
    assert result2 == [2, 4]

    # Test 3: Remove head node
    nums3, head3 = [1], create_linked_list([1, 2, 3])
    res3 = solver.modifiedList(nums3, head3)
    result3 = linked_list_to_list(res3)
    print("Test 3:", nums3, "[1,2,3]", "->", result3)
    assert result3 == [2, 3]

    # Test 4: Remove tail node
    nums4, head4 = [3], create_linked_list([1, 2, 3])
    res4 = solver.modifiedList(nums4, head4)
    result4 = linked_list_to_list(res4)
    print("Test 4:", nums4, "[1,2,3]", "->", result4)
    assert result4 == [1, 2]

    # Test 5: Remove all nodes
    nums5, head5 = [1, 2, 3], create_linked_list([1, 2, 3])
    res5 = solver.modifiedList(nums5, head5)
    result5 = linked_list_to_list(res5)
    print("Test 5:", nums5, "[1,2,3]", "->", result5)
    assert result5 == []

    # Test 6: Remove nothing (nums not in list)
    nums6, head6 = [5], create_linked_list([1, 2, 3])
    res6 = solver.modifiedList(nums6, head6)
    result6 = linked_list_to_list(res6)
    print("Test 6:", nums6, "[1,2,3]", "->", result6)
    assert result6 == [1, 2, 3]

    # Test 7: Single node list, remove it
    nums7, head7 = [1], create_linked_list([1])
    res7 = solver.modifiedList(nums7, head7)
    result7 = linked_list_to_list(res7)
    print("Test 7:", nums7, "[1]", "->", result7)
    assert result7 == []

    # Test 8: Single node list, keep it
    nums8, head8 = [2], create_linked_list([1])
    res8 = solver.modifiedList(nums8, head8)
    result8 = linked_list_to_list(res8)
    print("Test 8:", nums8, "[1]", "->", result8)
    assert result8 == [1]

    # Test 9: Remove consecutive nodes
    nums9, head9 = [2, 3], create_linked_list([1, 2, 3, 4])
    res9 = solver.modifiedList(nums9, head9)
    result9 = linked_list_to_list(res9)
    print("Test 9:", nums9, "[1,2,3,4]", "->", result9)
    assert result9 == [1, 4]

    # Test 10: Remove duplicates
    nums10, head10 = [2], create_linked_list([1, 2, 2, 3])
    res10 = solver.modifiedList(nums10, head10)
    result10 = linked_list_to_list(res10)
    print("Test 10:", nums10, "[1,2,2,3]", "->", result10)
    assert result10 == [1, 3]

    # Test 11: Empty nums list (remove nothing)
    nums11, head11 = [], create_linked_list([1, 2, 3])
    res11 = solver.modifiedList(nums11, head11)
    result11 = linked_list_to_list(res11)
    print("Test 11:", nums11, "[1,2,3]", "->", result11)
    assert result11 == [1, 2, 3]

    # Test 12: Longer list with multiple removals
    nums12, head12 = [2, 5, 7], create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    res12 = solver.modifiedList(nums12, head12)
    result12 = linked_list_to_list(res12)
    print("Test 12:", nums12, "[1,2,3,4,5,6,7,8]", "->", result12)
    assert result12 == [1, 3, 4, 6, 8]

    print("All tests passed!")


if __name__ == "__main__":
    test_modifiedList()