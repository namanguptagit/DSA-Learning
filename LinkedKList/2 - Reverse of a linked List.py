# Definition for singly-linked list.
from typing import Optional

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

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# Helper function to convert linked list to list for easy comparison
def linked_list_to_list(head):
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

# Test cases
def test_reverse_list():
    solution = Solution()
    
    # Test Case 1: Normal linked list [1,2,3,4,5]
    print("Test Case 1: [1,2,3,4,5]")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = solution.reverseList(head1)
    result1 = linked_list_to_list(reversed1)
    expected1 = [5, 4, 3, 2, 1]
    print(f"Input: [1,2,3,4,5]")
    print(f"Output: {result1}")
    print(f"Expected: {expected1}")
    print(f"Test Passed: {result1 == expected1}")
    print("-" * 40)
    
    # Test Case 2: Two nodes [1,2]
    print("Test Case 2: [1,2]")
    head2 = create_linked_list([1, 2])
    reversed2 = solution.reverseList(head2)
    result2 = linked_list_to_list(reversed2)
    expected2 = [2, 1]
    print(f"Input: [1,2]")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print(f"Test Passed: {result2 == expected2}")
    print("-" * 40)
    
    # Test Case 3: Single node [1]
    print("Test Case 3: [1]")
    head3 = create_linked_list([1])
    reversed3 = solution.reverseList(head3)
    result3 = linked_list_to_list(reversed3)
    expected3 = [1]
    print(f"Input: [1]")
    print(f"Output: {result3}")
    print(f"Expected: {expected3}")
    print(f"Test Passed: {result3 == expected3}")
    print("-" * 40)
    
    # Test Case 4: Empty list []
    print("Test Case 4: []")
    head4 = create_linked_list([])
    reversed4 = solution.reverseList(head4)
    result4 = linked_list_to_list(reversed4)
    expected4 = []
    print(f"Input: []")
    print(f"Output: {result4}")
    print(f"Expected: {expected4}")
    print(f"Test Passed: {result4 == expected4}")
    print("-" * 40)
    
    # Test Case 5: Large linked list [1,2,3,4,5,6,7,8,9,10]
    print("Test Case 5: [1,2,3,4,5,6,7,8,9,10]")
    head5 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    reversed5 = solution.reverseList(head5)
    result5 = linked_list_to_list(reversed5)
    expected5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Input: [1,2,3,4,5,6,7,8,9,10]")
    print(f"Output: {result5}")
    print(f"Expected: {expected5}")
    print(f"Test Passed: {result5 == expected5}")
    print("-" * 40)
    
    # Test Case 6: All same values [1,1,1,1]
    print("Test Case 6: [1,1,1,1]")
    head6 = create_linked_list([1, 1, 1, 1])
    reversed6 = solution.reverseList(head6)
    result6 = linked_list_to_list(reversed6)
    expected6 = [1, 1, 1, 1]
    print(f"Input: [1,1,1,1]")
    print(f"Output: {result6}")
    print(f"Expected: {expected6}")
    print(f"Test Passed: {result6 == expected6}")
    print("-" * 40)

# Run the tests
if __name__ == "__main__":
    test_reverse_list()