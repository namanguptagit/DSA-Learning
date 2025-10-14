# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else: return None

        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow

# Helper function to create a linked list from a list of values
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

# Helper function to create a cycle in linked list
def create_linked_list_with_cycle(values, cycle_pos):
    """
    Helper function to create a linked list with a cycle
    values: list of values for the linked list
    cycle_pos: position where the cycle starts (0-indexed), -1 means no cycle
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    cycle_node = None
    
    for i, val in enumerate(values[1:], 1):
        current.next = ListNode(val)
        current = current.next
        
        # Store reference to the node where cycle should start
        if i == cycle_pos:
            cycle_node = current
    
    # Create cycle if cycle_pos is valid
    if cycle_pos >= 0 and cycle_pos < len(values):
        current.next = cycle_node
    
    return head

# Helper function to find cycle start position for verification
def find_cycle_start_position(head):
    """Helper function to find the position where cycle starts"""
    if not head:
        return -1
    
    visited = {}
    current = head
    position = 0
    
    while current:
        if current in visited:
            return visited[current]
        visited[current] = position
        current = current.next
        position += 1
    
    return -1

def test_detect_cycle():
    """Test cases for the detect cycle function"""
    solution = Solution()
    
    # Test Case 1: Linked list with cycle starting at position 1
    print("Test Case 1: Linked list with cycle starting at position 1")
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    cycle_start1 = solution.detectCycle(head1)
    expected_pos1 = 1
    actual_pos1 = find_cycle_start_position(head1)
    print(f"Input: [3,2,0,-4] with cycle at position 1")
    print(f"Expected cycle start position: {expected_pos1}")
    print(f"Actual cycle start position: {actual_pos1}")
    print(f"Cycle detected: {cycle_start1 is not None}")
    print(f"Test 1 {'PASSED' if cycle_start1 is not None and actual_pos1 == expected_pos1 else 'FAILED'}\n")
    
    # Test Case 2: Linked list with cycle starting at position 0
    print("Test Case 2: Linked list with cycle starting at position 0")
    head2 = create_linked_list_with_cycle([1, 2], 0)
    cycle_start2 = solution.detectCycle(head2)
    expected_pos2 = 0
    actual_pos2 = find_cycle_start_position(head2)
    print(f"Input: [1,2] with cycle at position 0")
    print(f"Expected cycle start position: {expected_pos2}")
    print(f"Actual cycle start position: {actual_pos2}")
    print(f"Cycle detected: {cycle_start2 is not None}")
    print(f"Test 2 {'PASSED' if cycle_start2 is not None and actual_pos2 == expected_pos2 else 'FAILED'}\n")
    
    # Test Case 3: Linked list with no cycle
    print("Test Case 3: Linked list with no cycle")
    head3 = create_linked_list_with_cycle([1], -1)
    cycle_start3 = solution.detectCycle(head3)
    expected_pos3 = -1
    actual_pos3 = find_cycle_start_position(head3)
    print(f"Input: [1] with no cycle")
    print(f"Expected cycle start position: {expected_pos3}")
    print(f"Actual cycle start position: {actual_pos3}")
    print(f"Cycle detected: {cycle_start3 is not None}")
    print(f"Test 3 {'PASSED' if cycle_start3 is None and actual_pos3 == expected_pos3 else 'FAILED'}\n")
    
    # Test Case 4: Empty linked list
    print("Test Case 4: Empty linked list")
    head4 = create_linked_list_with_cycle([], -1)
    cycle_start4 = solution.detectCycle(head4)
    expected_pos4 = -1
    actual_pos4 = find_cycle_start_position(head4)
    print(f"Input: [] (empty list)")
    print(f"Expected cycle start position: {expected_pos4}")
    print(f"Actual cycle start position: {actual_pos4}")
    print(f"Cycle detected: {cycle_start4 is not None}")
    print(f"Test 4 {'PASSED' if cycle_start4 is None and actual_pos4 == expected_pos4 else 'FAILED'}\n")
    
    # Test Case 5: Single node with self-cycle
    print("Test Case 5: Single node with self-cycle")
    head5 = create_linked_list_with_cycle([1], 0)
    cycle_start5 = solution.detectCycle(head5)
    expected_pos5 = 0
    actual_pos5 = find_cycle_start_position(head5)
    print(f"Input: [1] with self-cycle")
    print(f"Expected cycle start position: {expected_pos5}")
    print(f"Actual cycle start position: {actual_pos5}")
    print(f"Cycle detected: {cycle_start5 is not None}")
    print(f"Test 5 {'PASSED' if cycle_start5 is not None and actual_pos5 == expected_pos5 else 'FAILED'}\n")
    
    # Test Case 6: Large linked list with cycle
    print("Test Case 6: Large linked list with cycle")
    head6 = create_linked_list_with_cycle([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    cycle_start6 = solution.detectCycle(head6)
    expected_pos6 = 3
    actual_pos6 = find_cycle_start_position(head6)
    print(f"Input: [1,2,3,4,5,6,7,8,9] with cycle at position 3")
    print(f"Expected cycle start position: {expected_pos6}")
    print(f"Actual cycle start position: {actual_pos6}")
    print(f"Cycle detected: {cycle_start6 is not None}")
    print(f"Test 6 {'PASSED' if cycle_start6 is not None and actual_pos6 == expected_pos6 else 'FAILED'}\n")
    
    # Test Case 7: Two nodes with cycle at second node
    print("Test Case 7: Two nodes with cycle at second node")
    head7 = create_linked_list_with_cycle([1, 2], 1)
    cycle_start7 = solution.detectCycle(head7)
    expected_pos7 = 1
    actual_pos7 = find_cycle_start_position(head7)
    print(f"Input: [1,2] with cycle at position 1")
    print(f"Expected cycle start position: {expected_pos7}")
    print(f"Actual cycle start position: {actual_pos7}")
    print(f"Cycle detected: {cycle_start7 is not None}")
    print(f"Test 7 {'PASSED' if cycle_start7 is not None and actual_pos7 == expected_pos7 else 'FAILED'}\n")

if __name__ == "__main__":
    test_detect_cycle()