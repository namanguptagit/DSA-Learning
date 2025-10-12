from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

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

def test_middle_node():
    """Test cases for the middle node function"""
    solution = Solution()
    
    # Test Case 1: Odd number of nodes [1,2,3,4,5] -> middle should be 3
    print("Test Case 1: Odd number of nodes")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    middle1 = solution.middleNode(head1)
    result1 = linked_list_to_list(middle1)
    expected1 = [3, 4, 5]
    print(f"Input: [1,2,3,4,5]")
    print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    print(f"Test 1 {'PASSED' if result1 == expected1 else 'FAILED'}\n")
    
    # Test Case 2: Even number of nodes [1,2,3,4,5,6] -> middle should be 4 (second middle)
    print("Test Case 2: Even number of nodes")
    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    middle2 = solution.middleNode(head2)
    result2 = linked_list_to_list(middle2)
    expected2 = [4, 5, 6]
    print(f"Input: [1,2,3,4,5,6]")
    print(f"Expected: {expected2}")
    print(f"Got: {result2}")
    print(f"Test 2 {'PASSED' if result2 == expected2 else 'FAILED'}\n")
    
    # Test Case 3: Single node [1] -> middle should be 1
    print("Test Case 3: Single node")
    head3 = create_linked_list([1])
    middle3 = solution.middleNode(head3)
    result3 = linked_list_to_list(middle3)
    expected3 = [1]
    print(f"Input: [1]")
    print(f"Expected: {expected3}")
    print(f"Got: {result3}")
    print(f"Test 3 {'PASSED' if result3 == expected3 else 'FAILED'}\n")
    
    # Test Case 4: Two nodes [1,2] -> middle should be 2
    print("Test Case 4: Two nodes")
    head4 = create_linked_list([1, 2])
    middle4 = solution.middleNode(head4)
    result4 = linked_list_to_list(middle4)
    expected4 = [2]
    print(f"Input: [1,2]")
    print(f"Expected: {expected4}")
    print(f"Got: {result4}")
    print(f"Test 4 {'PASSED' if result4 == expected4 else 'FAILED'}\n")
    
    # Test Case 5: Empty list [] -> should return None
    print("Test Case 5: Empty list")
    head5 = create_linked_list([])
    middle5 = solution.middleNode(head5)
    print(f"Input: []")
    print(f"Expected: None")
    print(f"Got: {middle5}")
    print(f"Test 5 {'PASSED' if middle5 is None else 'FAILED'}\n")
    
    # Test Case 6: Large odd list
    print("Test Case 6: Large odd list")
    head6 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    middle6 = solution.middleNode(head6)
    result6 = linked_list_to_list(middle6)
    expected6 = [5, 6, 7, 8, 9]
    print(f"Input: [1,2,3,4,5,6,7,8,9]")
    print(f"Expected: {expected6}")
    print(f"Got: {result6}")
    print(f"Test 6 {'PASSED' if result6 == expected6 else 'FAILED'}\n")

if __name__ == "__main__":
    test_middle_node()