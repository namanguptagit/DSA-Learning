from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False

# Test cases
def test_hasCycle():
    solution = Solution()
    
    # Test Case 1: No cycle - single node
    print("Test Case 1: Single node with no cycle")
    node1 = ListNode(1)
    result1 = solution.hasCycle(node1)
    print(f"Expected: False, Got: {result1}")
    assert result1 == False, "Test Case 1 failed"
    print("✓ Passed\n")
    
    # Test Case 2: No cycle - multiple nodes
    print("Test Case 2: Multiple nodes with no cycle")
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    result2 = solution.hasCycle(node1)
    print(f"Expected: False, Got: {result2}")
    assert result2 == False, "Test Case 2 failed"
    print("✓ Passed\n")
    
    # Test Case 3: Cycle exists - two nodes forming a cycle
    print("Test Case 3: Two nodes forming a cycle")
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1  # Creates a cycle
    result3 = solution.hasCycle(node1)
    print(f"Expected: True, Got: {result3}")
    assert result3 == True, "Test Case 3 failed"
    print("✓ Passed\n")
    
    # Test Case 4: Cycle exists - three nodes with cycle
    print("Test Case 4: Three nodes with cycle")
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node2  # Creates a cycle back to node2
    result4 = solution.hasCycle(node1)
    print(f"Expected: True, Got: {result4}")
    assert result4 == True, "Test Case 4 failed"
    print("✓ Passed\n")
    
    # Test Case 5: Cycle exists - four nodes with cycle
    print("Test Case 5: Four nodes with cycle")
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle back to node2
    result5 = solution.hasCycle(node1)
    print(f"Expected: True, Got: {result5}")
    assert result5 == True, "Test Case 5 failed"
    print("✓ Passed\n")
    
    # Test Case 6: Empty list
    print("Test Case 6: Empty list")
    result6 = solution.hasCycle(None)
    print(f"Expected: False, Got: {result6}")
    assert result6 == False, "Test Case 6 failed"
    print("✓ Passed\n")
    
    # Test Case 7: Self-loop (node points to itself)
    print("Test Case 7: Self-loop")
    node1 = ListNode(1)
    node1.next = node1  # Self-loop
    result7 = solution.hasCycle(node1)
    print(f"Expected: True, Got: {result7}")
    assert result7 == True, "Test Case 7 failed"
    print("✓ Passed\n")
    
    print("🎉 All test cases passed!")

if __name__ == "__main__":
    test_hasCycle()